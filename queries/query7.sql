-- Encontra os professores que ensinam "Digital Experience" no primeiro semestre de 2025
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
    d."Disc_ID" = 'CD9785'
    AND hp."Semestre" = 'Primeiro'
    AND hp."Ano" = '2025'
ORDER BY
    p."Nome";
