-- Problema 2621 - Quantidades Entre 10 e 20
-- https://judge.beecrowd.com/pt/problems/view/2621

SELECT pd.name
FROM products pd
JOIN providers pv ON pd.id_providers = pv.id
WHERE pd.amount >= 10 AND pd.amount < 20 AND pv.name LIKE 'P%';