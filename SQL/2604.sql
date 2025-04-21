-- Problema 2604 - Menores que 10 ou Maiores que 100
-- https://judge.beecrowd.com/pt/problems/view/2604

SELECT p.id,
       p.name
FROM products p
WHERE p.price < 10 
   OR p.price > 100;