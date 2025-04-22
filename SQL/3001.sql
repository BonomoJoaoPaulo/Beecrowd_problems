-- Problema 3001 - Update sem Where
-- https://judge.beecrowd.com/pt/problems/view/3001

SELECT 
    p.name,
    CASE p.type
        WHEN 'A' THEN 20.0
        WHEN 'B' THEN 70.0
        WHEN 'C' THEN 530.5
    END AS price
FROM 
    products p
ORDER BY 
    p.type,
    p.id DESC;