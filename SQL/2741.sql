-- Problema 2741 - Notas dos Alunos
-- https://judge.beecrowd.com/pt/problems/view/2741

SELECT ('Approved: ' || s.name), s.grade
FROM students s
WHERE s.grade >= 7
ORDER BY s.grade DESC;