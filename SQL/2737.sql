-- Problema 2737 - Advogados
-- https://judge.beecrowd.com/pt/problems/view/2737

-- SELECT advogado com mais clientes
(SELECT l.name, l.customers_number
FROM lawyers l
ORDER BY l.customers_number DESC
LIMIT 1)

UNION ALL

-- SELECT advogado com menos clientes
(SELECT l.name, l.customers_number
FROM lawyers l
ORDER BY l.customers_number ASC
LIMIT 1)

UNION ALL

-- Media de clientes por advogado
(SELECT 'Average' AS name, ROUND(AVG(l.customers_number)) AS customers_number
FROM lawyers l);