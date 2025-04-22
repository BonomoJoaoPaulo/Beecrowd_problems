-- Problema 2744 - Senhas
-- https://judge.beecrowd.com/pt/problems/view/2744

SELECT a.id, a.password, MD5(a.password) AS MD5
FROM account a;