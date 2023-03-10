-- Shows top 3 citiess with highest temperature
SELECT
    city,
    AVG(VALUE) AS avg_temp
FROM
    temperatures
WHERE
    month in ("7", "8")
GROUP BY
    city
ORDER BY
    avg_temp DESC
LIMIT
    3;
