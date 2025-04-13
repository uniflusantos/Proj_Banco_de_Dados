-- Encontra os alunos que cursaram disciplinas especificadas no mesmo semestre e ano (OR)
SELECT 
    a."Nome" AS nome_aluno,
    a."RA" AS ra_aluno,
    a."Curso" AS curso,
    h."Disc_Nome" AS disciplina,
    h."Semestre" AS semestre,
    h."Ano" AS ano
FROM 
    "Aluno" a
    JOIN "Historico_Aluno" h ON a."RA" = h."RA"
WHERE 
    h."Disc_Nome" IN ('Desenvolvimento Web', 'Banco de Dados')
    AND h."Semestre" = 'Primeiro' 
    AND h."Ano" = '2024'
ORDER BY
    h."Disc_Nome",
    a."Nome";
