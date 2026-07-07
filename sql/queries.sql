SELECT COUNT(*) FROM sales_data;

SELECT country, COUNT(*) AS customers
FROM sales_data
GROUP BY country
ORDER BY customers DESC;

SELECT AVG(sales) AS average_sales
FROM sales_data;

SELECT MAX(sales) AS highest_sale
FROM sales_data;

SELECT MIN(sales) AS lowest_sale
FROM sales_data;