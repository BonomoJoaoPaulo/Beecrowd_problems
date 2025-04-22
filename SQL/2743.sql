-- Problema 2743 - Quantidade de Caracteres
-- https://judge.beecrowd.com/pt/problems/view/2743

SELECT p.name, LENGTH(p.name) AS length
FROM people p
ORDER BY length DESC;