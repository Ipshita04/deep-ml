-- your query
SELECT company,total_profit
FROM (
    SELECT company, total_profit, DENSE_RANK() OVER (ORDER BY total_profit DESC) AS rn
    FROM(
        SELECT company,SUM(profit) AS total_profit
        FROM sales
        GROUP BY company
    )x
)t
WHERE rn<=3
ORDER BY total_profit DESC, company;
