-- Problema 2996 - Entrega de Pacotes
-- https://judge.beecrowd.com/pt/problems/view/2996

SELECT p.year AS year,
       s.name AS sender,
       r.name AS receiver
FROM packages p
JOIN users s ON p.id_user_sender = s.id
JOIN users r ON p.id_user_receiver = r.id
WHERE (p.color = 'blue' OR p.year = 2015) 
       AND NOT (s.address = 'Taiwan'
                OR r.address = 'Taiwan')
ORDER BY year DESC;