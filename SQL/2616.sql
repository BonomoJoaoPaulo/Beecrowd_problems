-- Problema 2616 - Nenhuma Locação
-- https://judge.beecrowd.com/pt/problems/view/2616

SELECT c.id, c.name
FROM customers c
WHERE c.id NOT IN (SELECT l.id_customers FROM locations l)
ORDER BY c.id;