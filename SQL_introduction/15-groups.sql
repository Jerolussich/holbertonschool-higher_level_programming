-- Shows score and frequency in table
SELECT
    score,
    COUNT(score) AS "number"
from
    second_table
GROUP BY
    score
ORDER BY
    number DESC;
