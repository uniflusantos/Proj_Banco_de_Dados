-- Query: Liste os cursos que são ministrados pelo professor 'PC5963', juntamente com os títulos dos cursos

SELECT DISTINCT 
    c."Curso_ID",
    c."Nome" AS nome_curso,
    d."Disc_ID",
    d."Nome" AS nome_disciplina,
    hp."Semestre",
    hp."Ano"
FROM "Historico_Professor" hp
JOIN "Disciplina" d ON hp."Disc_ID" = d."Disc_ID"
JOIN "Matriz_Curricular" mc ON d."Disc_ID" = mc."Disc_ID"
JOIN "Curso" c ON mc."Curso_ID" = c."Curso_ID"
WHERE hp."Prof_ID" = 'PC5963'
    AND hp."Ano" = '2025'
ORDER BY c."Nome", hp."Ano", hp."Semestre", d."Nome";
