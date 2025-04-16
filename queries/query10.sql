-- Query: Liste os IDs dos professores que ensinam matérias para mais de um curso

SELECT 
    hp."Prof_ID",
    p."Nome",
    COUNT(DISTINCT mc."Curso_ID") as num_cursos
FROM "Historico_Professor" hp
JOIN "Disciplina" d ON hp."Disc_ID" = d."Disc_ID"
JOIN "Matriz_Curricular" mc ON d."Disc_ID" = mc."Disc_ID"
JOIN "Professor" p ON hp."Prof_ID" = p."Prof_ID"
GROUP BY hp."Prof_ID", p."Nome"
HAVING COUNT(DISTINCT mc."Curso_ID") > 1
ORDER BY num_cursos DESC, p."Nome";
