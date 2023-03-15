-- Displays the top 3 cities temprature during July and August ordered by temp
SELECT city, AVG(value) AS avg_temp 
FROM tempratures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
