-- Problema 2995 - A Mensagem do Sensor
-- https://judge.beecrowd.com/pt/problems/view/2995

SELECT r.temperature, COUNT(*) AS number_of_records
FROM records r
GROUP BY r.mark, r.temperature
ORDER BY r.mark;