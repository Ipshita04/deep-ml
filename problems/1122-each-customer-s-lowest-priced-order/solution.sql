-- your query
SELECT MIN(order_id),customer_id,amount
FROM orders
WHERE (customer_id,amount) IN(
    SELECT customer_id,MIN(amount)
    FROM orders
    GROUP BY customer_id
)
GROUP BY customer_id,amount
ORDER BY customer_id;
