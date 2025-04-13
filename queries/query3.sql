--Query: Mostre a matriz curicular de pelo menos 2 cursos diferentes que possuem disciplinas em comum (e.g., Ciência da Computação e Ciência de Dados). Este exercício deve ser dividido em 2 queries sendo uma para cada curso;
SELECT
    m."Semestre",
    d."Disc_ID",
    d."Nome" AS "Disciplina"
FROM "Matriz_Curricular" m
JOIN "Disciplina" d ON m."Disc_ID" = d."Disc_ID"
JOIN "Curso" c ON m."Curso_ID" = c."Curso_ID"
WHERE c."Curso_ID" = 'C42'
ORDER BY m."Semestre"


SELECT
    m."Semestre",
    d."Disc_ID",
    d."Nome" AS "Disciplina"
FROM "Matriz_Curricular" m
JOIN "Disciplina" d ON m."Disc_ID" = d."Disc_ID"
JOIN "Curso" c ON m."Curso_ID" = c."Curso_ID"
WHERE c."Curso_ID" = 'C97'
ORDER BY m."Semestre"
