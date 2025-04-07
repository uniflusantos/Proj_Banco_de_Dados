-- Query: Encontre os nomes de todos os estudantes que cursaram "Ciência de Dados" (curso_id = 'C98')

SELECT DISTINCT 
    a."RA",
    a."Nome"
FROM "Aluno" a
WHERE a."Curso" = 'C98'
ORDER BY a."Nome";