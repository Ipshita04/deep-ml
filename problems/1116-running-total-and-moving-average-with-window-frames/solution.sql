-- your query
SELECT day,amount,running_total,moving_avg
FROM (
    SELECT day,amount, SUM(amount) OVER (ORDER BY day ROWS
    BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW ) AS running_total,
    AVG(amount) OVER (ORDER BY day ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_avg
    FROM sales
)
ORDER BY day