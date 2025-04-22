-- Problema 2739 - Dia do Pagamento
-- https://judge.beecrowd.com/pt/problems/view/2739

SELECT l.name, CAST(EXTRACT(DAY 
                    FROM l.payday) 
                    AS INTEGER)
FROM loan l;