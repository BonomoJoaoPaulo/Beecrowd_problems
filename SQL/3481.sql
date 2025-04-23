-- Problema 3481 - Classificando uma Árvore
-- https://judge.beecrowd.com/pt/problems/view/3481

SELECT DISTINCT n.node_id,
CASE
    WHEN n.pointer IS NULL THEN 'LEAF'
    WHEN n.node_id NOT IN (SELECT ns.pointer
                           FROM nodes ns
                           WHERE ns.pointer IS NOT NULL)
        THEN 'ROOT'
    ELSE 'INNER'
END AS type
FROM nodes n
ORDER BY n.node_id;