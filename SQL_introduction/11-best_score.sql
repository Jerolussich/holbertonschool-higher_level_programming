-- Shows score from table higher than 9
SELECT
    score,
    name
FROM
    second_table
WHERE
    score > 9
GROUP BY
    score,
    name
ORDER BY
    score DESC;
