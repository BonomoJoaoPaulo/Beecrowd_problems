-- Problema 2623 - Categorias com Vários Produtos
-- https://judge.beecrowd.com/pt/problems/view/2623

SELECT p.name, c.name
FROM products p
JOIN categories c ON p.id_categories = c.id
WHERE p.amount > 100 AND p.id_categories IN (1, 2, 3, 6, 9);