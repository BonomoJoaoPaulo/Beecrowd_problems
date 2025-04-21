-- Problema 2603 - Endereço dos Clientes
-- https://judge.beecrowd.com/pt/problems/view/2603

SELECT c.name,
       c.street
FROM customers c
WHERE c.city = 'Porto Alegre';