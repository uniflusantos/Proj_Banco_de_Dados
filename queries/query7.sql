-- Encontra os professores que ensinam "Orientação a Objetos" no segundo semestre de 2023
SELECT
    p."Prof_ID" AS id_professor,
    p."Nome" AS nome_professor,
    p."Departamento" AS departamento,
    d."Disc_ID" AS id_disciplina,
    d."Nome" AS nome_disciplina,
    hp."Semestre" AS semestre,
    hp."Ano" AS ano
FROM
    "Professor" p
    JOIN "Historico_Professor" hp ON p."Prof_ID" = hp."Prof_ID"
    JOIN "Disciplina" d ON hp."Disc_ID" = d."Disc_ID"
WHERE
    d."Disc_ID" = 'CC6753'
    AND hp."Semestre" = 'Segundo'
    AND hp."Ano" = '2023'
ORDER BY
    p."Nome";
