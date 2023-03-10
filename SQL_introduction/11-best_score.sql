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
