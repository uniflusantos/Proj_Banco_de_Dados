--Query: Liste todos os chefes de departamento e coordenadores de curso em apenas uma query de forma que a primeira coluna seja o nome do professor, a segunda o nome do departamento coordena e a terceira o nome do curso que coordena. Substitua os campos em branco do resultado da query pelo texto "nenhum"
SELECT 
    p."Nome" AS professor_nome,
    COALESCE(dep."Nome", 'nenhum') AS departamento_chefe,
    COALESCE(cur."Nome", 'nenhum') AS curso_coordenador
FROM "Professor" p
LEFT JOIN "Departamento" dep ON p."Prof_ID" = dep."Chefe"
LEFT JOIN "Curso" cur ON p."Prof_ID" = cur."Coordenador"
WHERE dep."Chefe" IS NOT NULL OR cur."Coordenador" IS NOT NULL;