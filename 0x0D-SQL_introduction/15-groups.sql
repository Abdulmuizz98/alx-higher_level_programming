-- List the number of records with the same score in the table 'second_table'.
-- in descending order of the count.
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
