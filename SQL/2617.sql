-- Problema 2617 - Fornecedor Ajax SA
-- https://judge.beecrowd.com/pt/problems/view/2617

SELECT pd.name, pv.name
FROM products pd
JOIN providers pv ON pd.id_providers = pv.id
WHERE pv.name = 'Ajax SA';