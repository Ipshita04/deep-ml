-- your query
SELECT MAX(daily_total) AS max_daily_total
FROM (
    SELECT SUM(amount) AS daily_total
    FROM orders
    WHERE order_date BETWEEN DATE'2024-01-01' AND '2024-01-31'
    GROUP BY order_date,customer_id
)t 