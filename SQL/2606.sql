-- Problema 2606 - Categorias
-- https://judge.beecrowd.com/pt/problems/view/2606

SELECT p.id, p.name
FROM products p
JOIN categories c ON p.id_categories = c.id
WHERE c.name LIKE 'super%';