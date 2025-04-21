-- Problema 2618 - Produtos Importados
-- https://judge.beecrowd.com/pt/problems/view/2618

SELECT pd.name, pv.name, c.name
FROM products pd
JOIN providers pv ON pd.id_providers = pv.id
JOIN categories c ON pd.id_categories = c.id
WHERE pv.name = 'Sansul SA' AND c.name = 'Imported';