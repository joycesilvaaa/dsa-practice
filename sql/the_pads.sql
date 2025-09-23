-- CTE (carrega antes a consulta)
-- union all, junta o resultado de duas querys

SELECT o.name || '(' || LEFT(o.occupation,1) || ')'
FROM occupations o
UNION ALL
SELECT 'There are a total of ' || COUNT(*) || ' ' || lower(o.occupation) || 's.' 
FROM occupations o
GROUP BY o.occupation -- agrupa por ocupação
ORDER BY 1; -- ordena da primeira consulta 


