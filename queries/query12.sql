-- Query: Encontre os estudantes que cursaram "Sistemas Digitais" ou "Conectividade e IOT"

SELECT DISTINCT 
    a."RA",
    a."Nome" as nome_aluno,
    ha."Disc_Nome" as nome_disciplina
FROM "Aluno" a
JOIN "Historico_Aluno" ha ON a."RA" = ha."RA"
WHERE ha."Disc_Nome" IN ('Sistemas Digitais', 'Conectividade e IOT')
ORDER BY a."Nome", ha."Disc_Nome";