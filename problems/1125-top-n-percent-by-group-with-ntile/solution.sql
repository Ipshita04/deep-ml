-- your query
SELECT region,MAX(amount)
FROM sales
GROUP BY region

