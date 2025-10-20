SELECT score AS "score",
    COUNT(score) AS "number"
FROM second_table
GROUP BY score;
