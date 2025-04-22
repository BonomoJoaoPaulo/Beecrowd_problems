-- Problema 2994 - Quanto Ganha um Médico?
-- https://judge.beecrowd.com/pt/problems/view/2994

WITH shift_payments AS (
    SELECT a.id, a.id_doctor, ((a.hours * 150) 
                         * ((100 + ws.bonus)
                            * 0.01)
                        ) as payment
    FROM attendances a
    JOIN work_shifts ws 
         ON a.id_work_shift = ws.id
)

SELECT d.name, ROUND(SUM(sp.payment), 1) as salary
FROM doctors d
JOIN shift_payments sp ON d.id = sp.id_doctor
GROUP BY d.name
ORDER BY salary DESC;