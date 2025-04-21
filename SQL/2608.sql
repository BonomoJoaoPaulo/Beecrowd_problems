-- Problema 2608 - Maior e Menor Preço
-- https://judge.beecrowd.com/pt/problems/view/2608

SELECT MAX(p.price),
       MIN(p.price)
FROM products p;