-- Problema 2738 - Concurso
-- https://judge.beecrowd.com/pt/problems/view/2738

SELECT c.name AS name, ROUND(((s.math * 2 + 
                               s.specific * 3 + 
                               s.project_plan * 5)/10), 2) AS avg
FROM candidate c
JOIN score s ON c.id = s.candidate_id
ORDER BY avg DESC;