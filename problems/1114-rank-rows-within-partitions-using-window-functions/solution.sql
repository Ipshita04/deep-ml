-- your query
SELECT department,employee,score,rn,rnk,dense_rnk
FROM(
    SELECT department,employee,score,ROW_NUMBER() OVER(PARTITION BY department ORDER BY score DESC,employee) AS rn, RANK() OVER(PARTITION BY department ORDER BY score DESC) AS rnk, DENSE_RANK() OVER(PARTITION BY department ORDER BY score DESC) AS dense_rnk
    FROM scores
)t
ORDER BY department,score DESC,employee
