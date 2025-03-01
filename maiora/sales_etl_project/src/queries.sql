SELECT COUNT(*) 
FROM sales_data;

SELECT region, SUM(total_sales) AS total_sales_amount 
FROM sales_data GROUP BY region;

SELECT AVG(total_sales) AS average_sales_amount 
FROM sales_data;

-- Ensure there are no duplicate id values
SELECT id, COUNT(*) 
FROM sales_data 
GROUP BY OrderId 
HAVING COUNT(*) > 1;