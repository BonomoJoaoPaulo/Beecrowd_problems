-- Problema 2619 - Super Luxo
-- https://judge.beecrowd.com/pt/problems/view/2619

SELECT pd.name, pv.name, pd.price
FROM products pd
JOIN providers pv ON pd.id_providers = pv.id
JOIN categories c ON pd.id_categories = c.id
WHERE pd.price > 1000 AND c.name = 'Super Luxury';