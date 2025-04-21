-- Problema 2620 - Pedidos no Primeiro Semestre
-- https://judge.beecrowd.com/pt/problems/view/2620

SELECT c.name, o.id
FROM orders o
JOIN customers c ON o.id_customers = c.id
WHERE EXTRACT(YEAR FROM o.orders_date) = 2016
  AND EXTRACT(MONTH FROM o.orders_date) < 7;