-- Problema 2746 - Vírus
-- https://judge.beecrowd.com/pt/problems/view/2746

SELECT REPLACE(v.name, 'H1', 'X')
FROM virus v;