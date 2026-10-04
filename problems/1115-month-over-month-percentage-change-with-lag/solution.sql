SELECT
    month,
    total,
    ROUND((total - prevtotal) / prevtotal * 100, 2) AS pct_change
FROM (
    SELECT
        month,
        total,
        LAG(total) OVER (ORDER BY month) AS prevtotal
    FROM (
        SELECT
            DATE_TRUNC('month', sale_date) AS month,
            SUM(amount) AS total
        FROM sales
        GROUP BY DATE_TRUNC('month', sale_date)
    ) t1
) t2
ORDER BY month;