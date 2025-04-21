-- Problema 2624 - Quantidades de Cidades por Clientes
-- https://judge.beecrowd.com/pt/problems/view/2624

SELECT COUNT(DISTINCT c.city)
FROM customers c;