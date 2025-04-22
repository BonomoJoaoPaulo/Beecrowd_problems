-- Problema 2742 - O Multiverso de Richard
-- https://judge.beecrowd.com/pt/problems/view/2742

SELECT lr.name AS name, ROUND(lr.omega * 1.618, 3) AS fator_N
FROM life_registry lr
JOIN dimensions d ON lr.dimensions_id = d.id
WHERE d.name IN ('C875', 'C774')
  AND lr.name LIKE 'Richard%'
ORDER BY fator_N;