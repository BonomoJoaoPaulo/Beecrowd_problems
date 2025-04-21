-- Problema 2614 - Locações de Setembro
-- https://judge.beecrowd.com/pt/problems/view/2614

SELECT c.name, r.rentals_date
FROM rentals r
JOIN customers c ON r.id_customers = c.id
WHERE EXTRACT(YEAR FROM r.rentals_date) = 2016
  AND EXTRACT(MONTH FROM r.rentals_date) = 9;