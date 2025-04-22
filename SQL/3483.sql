-- Problema 3483 - Segundo Maior e Menor
-- https://judge.beecrowd.com/pt/problems/view/3483

(SELECT c.city_name, c.population
FROM cities c
ORDER BY c.population DESC
OFFSET 1 LIMIT 1)

UNION ALL

(SELECT c.city_name, c.population
FROM cities c
ORDER BY c.population
OFFSET 1 LIMIT 1);