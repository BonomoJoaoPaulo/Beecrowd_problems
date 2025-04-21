-- Problema 2610 - Valor Médio dos Produtos
-- https://judge.beecrowd.com/pt/problems/view/2610

SELECT ROUND(AVG(price), 2)
FROM products p;