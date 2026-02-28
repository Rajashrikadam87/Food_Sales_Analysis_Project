import pandas as pd 
import zipfile
zip_file=zipfile.ZipFile(r"C:\Users\Admin\Downloads\Orders Data.zip") # Need use path bacause of file not found error
dfs=[]   # Created Empty list

for file in zip_file.namelist():  # use lops beacuse there is posibilty of differnt files to avoid other files 
  if file.endswith(".xlsx"):
      df=pd.read_excel(zip_file.open(file))  # read excel file 
      dfs.append(df)                         # append all files in single
      
orders=pd.concat(dfs, ignore_index=True)     # made one DataFrame
orders.head()                                 
orders.shape

food=pd.read_excel(r"C:\Users\Admin\Downloads\Other_Data.xlsx")   # load another needed  file 
food.head()
food.dtypes

# standerdize column name  Fooditem into ItemCode to avoid error while merging according key

orders.rename(columns={"Fooditem":"ItemCode"}, inplace=True)
orders.head()

# merging two tables orders and food

final_df=pd.merge(orders , food ,on="ItemCode",how="left")  # use left join beacuse we need all orders for analysis
final_df.head()

#Converting date column due avoid text or other data in future

final_df["orderDate"]=pd.to_datetime(final_df["orderDate"])

# Creating Month and Date column for further analysis

final_df['Month'] = final_df['orderDate'].dt.month_name()
final_df['Day'] = final_df['orderDate'].dt.day_name()

# finding missing values

final_df.isnull().sum()

# .................Analysis on Data..........................

#Monthly revenue

final_df["Amount"]=final_df["quantity"]*final_df["Price"] # need to create column for mothly analysis
final_df.columns

final_df.groupby("Month")["Amount"].sum()

# Q1.Is revenue growing or falling 

final_df['Month_Number'] = final_df['orderDate'].dt.month  # need to cearte to avoid alphabetical sort

final_df.groupby("Month")["Amount"].sum().sort_index()

# Q2.Top revenue Generating products

final_df.groupby("Food Name")["Amount"].sum().sort_values(ascending=False).head(10)

# Q3.which Catogary earns most 

final_df.groupby("Food_Type")["Amount"].sum().sort_values(ascending=False)

# Q4.Avrage order value

final_df["Amount"].mean()

# Q5.Monthly order count

final_df.groupby("Month")["ItemCode"].count()

# Revenue Day & month

pivot = final_df.pivot_table(
    values="Amount",
    index=["Month_Number","Month"],
    columns="Day",
    aggfunc="sum"
)
pivot.reset_index(level=0, drop=True)
pivot

#.............Analysis Completed...........

import os

output_path = r"C:\Users\Admin\Desktop\Food_Sales_Analysis_Project\Output"
os.makedirs(output_path, exist_ok=True)  # creates folder if missing


final_df.to_excel(os.path.join(output_path, "Final_Cleaned_Data.xlsx"), index=False)
pivot.to_excel(os.path.join(output_path, "Revenue_Pivot.xlsx"))