-- your query
SELECT recorded_on
FROM(
    SELECT recorded_on,temperature,LAG(temperature) OVER (ORDER BY recorded_on) AS prevtemp
    FROM weather
)t
WHERE temperature>prevtemp
ORDER BY recorded_on
