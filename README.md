**\*\*Food Sales Analysis Project:**



This project analyzes food sales data from multiple sources to generate insights on revenue, top-selling items, and order trends. It demonstrates data cleaning, merging, transformation, and analysis using Python and Pandas.



**\*\*Project Overview:**



**The dataset includes:**



\*Orders Data: Order details like order\_id, orderDate, customer\_id, Restaurant\_ID, Fooditem, quantity,   deliver\_status, payment\_method.



\*Food Data: Food master details like ItemCode, Food Name, Price, Food\_Type.



\*\*Goal: Clean, merge, and analyze these datasets to understand sales trends, monthly revenue, top products, and category performance.



**Project Structure:**



Food\_Sales\_Analysis\_Project/

├── data/             # Raw datasets (Excel)

├── output/           # Result Excel files and pivot tables

├── analysis.py       # Python script for data cleaning and analysis

├── README.md         # Project documentation

├── requirements.txt  # Required Python libraries



**Tools \& Libraries:**



Python 3.x

Pandas

Zipfile (for reading zipped data files)

Excel (for output)





**\*\*Analysis Performed\*\***



1\. **Data Cleaning \& Merging**



Loaded multiple Excel files from a zip archive using Pandas.



Standardized column names (Fooditem → ItemCode).



Merged orders and food master tables using a left join.



Converted date columns and created Month and Day columns.



Checked for missing values.



**2. Revenue Analysis**



Calculated monthly revenue (Amount = quantity \* Price).



Tracked revenue growth month-wise.



Created a pivot table for revenue by day and month.



**3. Top Products \& Categories**



Identified top 10 revenue-generating food items.



Found the highest-earning food categories.



**4. Other Metrics**



Average order value.



Monthly order count.



**\*\*\*Outputs**



After running analysis.py, the following Excel files are generated in output/:



Final\_Cleaned\_Data.xlsx → Cleaned and merged dataset with added columns.



Revenue\_Pivot.xlsx → Pivot table showing revenue per day and month.



**\*\*\*How to Run\*\*\***



***Install required Python packages:***



pip install pandas openpyxl



***Run the analysis script:***



python analysis.py



***Check the output/ folder for results.***



**\*\*Key Insights\*\***



**Top-selling items:**



1.Butter Chicken



2.Chole Bhature



3.Tandoori Chicken



**Highest revenue category (Food\_Type):** Main Course



**Monthly revenue trend:** Increase from January to March, then decrease in April



**Average order value:** 915.98



**Author**



Rajashri Kadam

MSc Computer Science | Aspiring Data Analyst



