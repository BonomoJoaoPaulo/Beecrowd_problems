-- Problema 2745 - Taxas
-- https://judge.beecrowd.com/pt/problems/view/2745

SELECT p.name, ROUND(p.salary * 0.1, 2) AS tax
FROM people p
WHERE p.salary > 3000;