--Query: Mostre todos os TCCs orientados por um professor junto com os nomes dos alunos que fizeram o projeto;
SELECT
    t."TCC_ID",
    t."Titulo",
    a."Nome" AS aluno_nome
FROM "TCC" t
JOIN "TCC_Aluno" ta ON t."TCC_ID" = ta."TCC_ID"
JOIN "Aluno" a ON ta."RA" = a."RA"
WHERE t."Orientador" = 'PD3491';