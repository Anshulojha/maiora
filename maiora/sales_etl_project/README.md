# Sales Data ETL Process

This Python script performs an ETL (Extract, Transform, Load) process for sales data from two different regions and loads the transformed data into an SQLite database. The script extracts data from two CSV files, applies business rules to clean and process the data, and then loads it into a database for further analysis.

---

## Table of Contents

1. [Overview](#overview)
2. [Business Rules](#business-rules)
3. [Setup and Requirements](#setup-and-requirements)
4. [How to Run the Program](#how-to-run-the-program)
5. [SQL Validation Queries](#sql-validation-queries)
6. [Assumptions and Decisions](#assumptions-and-decisions)
7. [License](#license)

---

## Overview

The script processes sales data from two CSV files, one for each region. It performs the following tasks:

- **Extract**: Reads data from CSV files for two regions (`order_region_a.csv` and `order_region_b.csv`).
- **Transform**: Applies the following business rules to the data:
    - Calculates `total_sales` as the product of `QuantityOrdered` and `ItemPrice`.
    - Adds a `region` column to identify the region (A or B).
    - Calculates `net_sale` as `total_sales` minus `PromotionDiscount`.
    - Removes duplicate records based on `OrderId`.
    - Filters out records where `net_sale <= 0`.
- **Load**: Loads the transformed data into an SQLite database (`sales_data.db`).
- **Validate**: SQL queries are provided to validate the data in the database.

---

## Business Rules

- **Combine the data from both regions**: The data from both regions (A and B) is combined into a single table.
- **Calculate `total_sales`**: This is calculated as `QuantityOrdered * ItemPrice`.
- **Add `region` column**: Identifies the region (A or B) for each record.
- **Remove duplicate `OrderId` values**: Ensures each order is unique based on `OrderId`.
- **Calculate `net_sale`**: This is calculated as `total_sales - PromotionDiscount`.
- **Exclude orders where `net_sale <= 0`**: Only include orders where the sales after discount are positive.

---

## Setup and Requirements

Before running the script, ensure the following dependencies are installed:

1. **Python 3.x**
2. **pandas** library
    - You can install it via pip if you don't have it already:
      ```bash
      pip install pandas
      ```
3. **sqlite3** (typically included with Python)

Additionally, ensure that the following CSV files are available in the same directory as the script:

- `order_region_a.csv`
- `order_region_b.csv`

These files contain the sales data for regions A and B.

---

## How to Run the Program

1. **Clone the repository** or download the script to your local machine.
2. **Place the CSV files** (`order_region_a.csv` and `order_region_b.csv`) in the same directory as the Python script.
3. **Run the script**:
    ```bash
    python script_name.py
    ```
   - Replace `script_name.py` with the actual name of the Python script.
4. The program will:
    - Read the sales data from the CSV files.
    - Apply the business rules.
    - Combine the data into a single table.
    - Load the transformed data into the SQLite database (`sales_data.db`).

---

## SQL Validation Queries

Once the data is loaded into the SQLite database, you can use the following SQL queries to validate the data:

1. **Count the Total Number of Records**:
    ```sql
    SELECT COUNT(*) FROM sales_data;
    ```

2. **Find the Total Sales Amount by Region**:
    ```sql
    SELECT region, SUM(total_sales) AS total_sales_by_region
    FROM sales_data
    GROUP BY region;
    ```

3. **Find the Average Sales Amount Per Transaction**:
    ```sql
    SELECT AVG(total_sales) AS average_sales_per_transaction
    FROM sales_data;
    ```

4. **Ensure There Are No Duplicate OrderIds**:
    ```sql
    SELECT OrderId, COUNT(*) 
    FROM sales_data 
    GROUP BY OrderId 
    HAVING COUNT(*) > 1;
    ```

---

## Assumptions and Decisions

1. **Business Rules**: The script follows the exact business rules as outlined in the task description:
    - `total_sales` is calculated as `QuantityOrdered * ItemPrice`.
    - `net_sale` is calculated as `total_sales - PromotionDiscount`.
    - Only orders with a positive `net_sale` are included.

2. **Data Integrity**: The script removes duplicate records based on `OrderId` to ensure each order is unique.

3. **Database Choice**: SQLite is chosen because it is lightweight and doesn’t require an external server setup. It is suitable for this small-scale ETL task.

4. **File Locations**: The CSV files (`order_region_a.csv` and `order_region_b.csv`) are expected to be in the same directory as the Python script. Ensure these files are properly formatted before running the script.

---

## License

This project is not under any licensed now.