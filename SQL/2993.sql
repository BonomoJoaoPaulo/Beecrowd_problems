-- Problema 2993 - Mais Frequente
-- https://judge.beecrowd.com/pt/problems/view/2993

SELECT COUNT(vt.amount) AS amount_occurrence
FROM value_table vt
GROUP BY vt.amount
ORDER BY amount_occurrence
LIMIT 1;