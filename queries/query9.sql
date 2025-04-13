-- Query: Encontre os nomes de todos os estudantes que cursaram "Ciência de Dados" 
SELECT DISTINCT 
    a."RA",
    a."Nome"
FROM "Aluno" a
WHERE a."Curso" = 'C42'
ORDER BY a."Nome";
