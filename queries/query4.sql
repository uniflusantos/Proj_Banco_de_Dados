--Query: Para um determinado aluno, mostre os códigos e nomes das disciplinas já cursadas junto com os nomes dos professores que lecionaram a disciplina para o aluno, juntamente com o semestre em que a disciplina foi cursada pelo aluno;
SELECT
    ha."Disc_ID",
    ha."Disc_Nome",
    p."Nome" AS professor_nome,
    p."Prof_ID" AS professor_id,
    ha."Semestre",
    ha."Ano"
FROM
    "Historico_Aluno" ha
    JOIN "Historico_Professor" hp ON ha."Disc_ID" = hp."Disc_ID"
    AND ha."Semestre" = hp."Semestre"
    AND ha."Ano" = hp."Ano"
    JOIN "Professor" p ON hp."Prof_ID" = p."Prof_ID"
WHERE
    ha."RA" = 'A4570'
ORDER BY
    ha."Ano",
    ha."Semestre",
    ha."Disc_ID";
