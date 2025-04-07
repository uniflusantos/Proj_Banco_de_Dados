-- Query: Recupere os nomes de todos os estudantes que cursaram "Fundamentos de Algoritmos" (course_id = 'CC8882') no segundo semestre de 2024

SELECT DISTINCT
    a."RA",
    a."Nome" as nome_aluno,
    ha."Semestre",
    ha."Ano"
FROM "Aluno" a
JOIN "Historico_Aluno" ha ON a."RA" = ha."RA"
WHERE ha."Disc_ID" = 'CC8882'
    AND ha."Semestre" = 'Segundo'
    AND ha."Ano" = '2024'
ORDER BY a."Nome";