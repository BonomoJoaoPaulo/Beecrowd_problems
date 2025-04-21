-- Problema 2605 - Representantes Executivos
-- https://judge.beecrowd.com/pt/problems/view/2605

SELECT 
    pd.name AS product_name,
    pv.name AS provider_name
FROM products pd
JOIN providers pv ON pd.id_providers = pv.id
JOIN categories c ON pd.id_categories = c.id
WHERE c.id = 6;