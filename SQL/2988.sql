-- Problema 2988 - Campeonato Cearense
-- https://judge.beecrowd.com/pt/problems/view/2988

WITH all_matches AS (
    SELECT
        team_1 AS team_id,
        team_1_goals AS goals_for,
        team_2_goals AS goals_against
    FROM matches
    UNION ALL
    SELECT
        team_2 AS team_id,
        team_2_goals AS goals_for,
        team_1_goals AS goals_against
    FROM matches
),
results AS (
    SELECT
        team_id,
        COUNT(*) AS games_played,
        SUM(CASE WHEN goals_for > goals_against THEN 1 ELSE 0 END) AS wins,
        SUM(CASE WHEN goals_for = goals_against THEN 1 ELSE 0 END) AS draws,
        SUM(CASE WHEN goals_for < goals_against THEN 1 ELSE 0 END) AS losses,
        SUM(CASE 
            WHEN goals_for > goals_against THEN 3
            WHEN goals_for = goals_against THEN 1
            ELSE 0
        END) AS points
    FROM all_matches
    GROUP BY team_id
)
SELECT
    t.name AS name,
    r.games_played AS matches,
    r.wins AS victories,
    r.losses AS defeats,
    r.draws AS draws,
    r.points AS score
FROM results r
JOIN teams t ON t.id = r.team_id
ORDER BY score DESC;