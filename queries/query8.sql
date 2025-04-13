-- Query: Recupere os IDs dos estudantes que não estão matriculados em nenhum curso do departamento de "Ciência de Dados"

SELECT DISTINCT a."RA", a."Nome"
FROM "Aluno" a
WHERE a."Curso" NOT IN (
    SELECT c."Curso_ID"
    FROM "Curso" c
    JOIN "Matriz_Curricular" mc ON c."Curso_ID" = mc."Curso_ID"
    JOIN "Disciplina" d ON mc."Disc_ID" = d."Disc_ID"
    WHERE d."Departamento" = 'DD84'
)
ORDER BY a."RA";
