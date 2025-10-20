-- prints number of time of a score
SELECT score AS "score",
    COUNT(score) AS "number"
FROM second_table
GROUP BY score
ORDER BY number DESC;
