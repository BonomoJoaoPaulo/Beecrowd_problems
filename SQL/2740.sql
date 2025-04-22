-- Problema 2740 - Liga
-- https://judge.beecrowd.com/pt/problems/view/2740

WITH podium AS (
    SELECT l.position, 'Podium: ' || l.team AS result
    FROM league l
    ORDER BY l.position
    LIMIT 3
),
demoted AS (
    SELECT l.position, 'Demoted: ' || l.team AS result
    FROM league l
    ORDER BY l.position DESC
    LIMIT 2
),
all_results AS (
    SELECT * FROM podium
    UNION ALL
    SELECT * FROM demoted
)

SELECT result AS name
FROM all_results
ORDER BY position;