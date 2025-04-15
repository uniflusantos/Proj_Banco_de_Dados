-- Encontra os estudantes que cursaram "Fundamentos de Algoritmos" e "Cálculo I" no mesmo semestre 
SELECT 
    a."Nome" AS nome_aluno,
    a."RA" AS ra_aluno,
    h1."Semestre" AS semestre,
    h1."Ano" AS ano
FROM 
    "Aluno" a
JOIN 
    "Historico_Aluno" h1 ON a."RA" = h1."RA"
JOIN 
    "Historico_Aluno" h2 ON a."RA" = h2."RA" 
    AND h1."Semestre" = h2."Semestre" 
    AND h1."Ano" = h2."Ano"
WHERE 
    h1."Disc_Nome" = 'Fundamentos de Algoritmos'
    AND h2."Disc_Nome" = 'Cálculo I'
ORDER BY 
    a."Nome", 
    h1."Ano", 
    h1."Semestre";-- Query: Encontre os nomes de todos os estudantes
SELECT 
    "RA",
    "Nome"
FROM "Aluno"
ORDER BY "Nome";
