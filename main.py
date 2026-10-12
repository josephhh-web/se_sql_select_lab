# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd  # pyright: ignore[reportMissingModuleSource]

# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')
 
# STEP 2
# Replace None with your code
df_first_five = pd.read_sql("SELECT employeeNumber, lastName FROM employees;", conn)

# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql("SELECT lastName, employeeNumber FROM employees ORDER BY employeeNumber DESC;", conn)

# STEP 4
# Replace None with your code
df_alias = pd.read_sql("SELECT employeeNumber AS ID, firstName AS name FROM employees;", conn)

# STEP 5
# Replace None with your code
df_executive = pd.read_sql("SELECT *, jobTitle AS role FROM employees WHERE jobTitle = 'President';",conn)

# STEP 6
# Replace None with your code
df_name_length = pd.read_sql("SELECT lastName, LENGTH(lastName) AS name_length FROM employees;", conn)

# STEP 7
# Replace None with your code
df_short_title = pd.read_sql("SELECT *, SUBSTR(jobTitle, 1, 2) AS short_title FROM employees WHERE LENGTH(jobTitle) < 10;", conn)

# STEP 8
# Replace None with your code
sum_total_price = pd.read_sql("SELECT SUM(quantityOrdered * priceEach) FROM orderdetails;", conn).iloc[:, 0]

# STEP 9
# Replace None with your code
df_day_month_year = pd.read_sql("""
    SELECT 
        strftime('%d', orderDate) AS day, 
        strftime('%m', orderDate) AS month, 
        strftime('%Y', orderDate) AS year 
    FROM orders 
    ORDER BY orderDate;
""", conn)

conn.close()