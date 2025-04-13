-- Query: Liste os cursos que foram ministrados pelos professores 'PD6150' e 'PC5833'

SELECT DISTINCT 
    c."Curso_ID",
    c."Nome" AS nome_curso,
    d."Disc_ID",
    d."Nome" AS nome_disciplina,
    p."Nome" AS nome_professor,
    hp."Semestre",
    hp."Ano"
FROM "Historico_Professor" hp
JOIN "Professor" p ON hp."Prof_ID" = p."Prof_ID"
JOIN "Disciplina" d ON hp."Disc_ID" = d."Disc_ID"
JOIN "Matriz_Curricular" mc ON d."Disc_ID" = mc."Disc_ID"
JOIN "Curso" c ON mc."Curso_ID" = c."Curso_ID"
WHERE hp."Prof_ID" IN ('PD6150', 'PC5833')
ORDER BY c."Nome", d."Nome", p."Nome", hp."Ano", hp."Semestre";
