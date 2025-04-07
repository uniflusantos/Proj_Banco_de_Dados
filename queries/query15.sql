-- Query: Liste os cursos que foram ministrados por mais de um professor em semestres diferentes

WITH DisciplinaProfessores AS (
    SELECT 
        d."Disc_ID",
        d."Nome" AS nome_disciplina,
        COUNT(DISTINCT hp."Prof_ID") as num_professores,
        COUNT(DISTINCT (hp."Semestre", hp."Ano")) as num_semestres
    FROM "Disciplina" d
    JOIN "Historico_Professor" hp ON d."Disc_ID" = hp."Disc_ID"
    GROUP BY d."Disc_ID", d."Nome"
    HAVING COUNT(DISTINCT hp."Prof_ID") > 1
        AND COUNT(DISTINCT (hp."Semestre", hp."Ano")) > 1
)
SELECT 
    dp."Disc_ID",
    dp."nome_disciplina",
    p."Nome" AS nome_professor,
    hp."Semestre",
    hp."Ano"
FROM DisciplinaProfessores dp
JOIN "Historico_Professor" hp ON dp."Disc_ID" = hp."Disc_ID"
JOIN "Professor" p ON hp."Prof_ID" = p."Prof_ID"
ORDER BY dp."nome_disciplina", hp."Ano", hp."Semestre", p."Nome";