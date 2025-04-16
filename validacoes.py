import psycopg2
from psycopg2 import Error
from datetime import datetime

def conectar_banco():
    try:
        connection = psycopg2.connect(
            database="postgres",
            user="postgres.plfcanmzyxajqkpqyiov",
            password="Foguete50",
            host="aws-0-sa-east-1.pooler.supabase.com",
            port="5432"
        )
        return connection
    except (Exception, Error) as error:
        log_message = f"Erro ao conectar ao PostgreSQL: {error}"
        escrever_log(log_message)
        return None

def escrever_log(mensagem):
    with open('validacao_banco.log', 'a', encoding='utf-8') as arquivo_log:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        arquivo_log.write(f"[{timestamp}] {mensagem}\n")

def validar_regras():
    # Criar cabeçalho do log
    escrever_log("\n" + "="*50)
    escrever_log("INÍCIO DA VALIDAÇÃO DO BANCO DE DADOS")
    escrever_log("="*50 + "\n")

    connection = conectar_banco()
    if not connection:
        return
    
    cursor = connection.cursor()
    total_registros = {
        'alunos': 0,
        'cursos': 0,
        'departamentos': 0,
        'professores': 0,
        'disciplinas': 0,
        'tccs': 0
    }
    total_violacoes = 0
    
    try:
        # Contagem total de registros
        cursor.execute('SELECT COUNT(*) FROM "Aluno"')
        total_registros['alunos'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM "Curso"')
        total_registros['cursos'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM "Departamento"')
        total_registros['departamentos'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM "Professor"')
        total_registros['professores'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM "Disciplina"')
        total_registros['disciplinas'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM "TCC"')
        total_registros['tccs'] = cursor.fetchone()[0]

        escrever_log("RESUMO DO BANCO:")
        escrever_log(f"Total de Alunos: {total_registros['alunos']}")
        escrever_log(f"Total de Cursos: {total_registros['cursos']}")
        escrever_log(f"Total de Departamentos: {total_registros['departamentos']}")
        escrever_log(f"Total de Professores: {total_registros['professores']}")
        escrever_log(f"Total de Disciplinas: {total_registros['disciplinas']}")
        escrever_log(f"Total de TCCs: {total_registros['tccs']}\n")
        
        # 1. Todo aluno deve ter curso
        escrever_log("\nVALIDAÇÃO 1: Alunos sem curso")
        cursor.execute('''
            SELECT "RA", "Nome" 
            FROM "Aluno" 
            WHERE "Curso" IS NULL OR "Curso" = '';
        ''')
        alunos_sem_curso = cursor.fetchall()
        if alunos_sem_curso:
            total_violacoes += len(alunos_sem_curso)
            escrever_log(f"Foram encontrados {len(alunos_sem_curso)} alunos sem curso:")
            for aluno in alunos_sem_curso:
                escrever_log(f"RA: {aluno[0]}, Nome: {aluno[1]}")
        else:
            escrever_log("✓ Todos os alunos possuem curso atribuído")

        # 2. Todo curso deve ter coordenador
        escrever_log("\nVALIDAÇÃO 2: Cursos sem coordenador")
        cursor.execute('''
            SELECT "Curso_ID", "Nome" 
            FROM "Curso" 
            WHERE "Coordenador" IS NULL OR "Coordenador" = '';
        ''')
        cursos_sem_coord = cursor.fetchall()
        if cursos_sem_coord:
            total_violacoes += len(cursos_sem_coord)
            escrever_log(f"Foram encontrados {len(cursos_sem_coord)} cursos sem coordenador:")
            for curso in cursos_sem_coord:
                escrever_log(f"ID: {curso[0]}, Nome: {curso[1]}")
        else:
            escrever_log("OK -> Todos os cursos possuem coordenador atribuído")

        # 3. Todo departamento deve ter chefe
        escrever_log("\nVALIDAÇÃO 3: Departamentos sem chefe")
        cursor.execute('''
            SELECT "Dept_ID", "Nome" 
            FROM "Departamento" 
            WHERE "Chefe" IS NULL OR "Chefe" = '';
        ''')
        deps_sem_chefe = cursor.fetchall()
        if deps_sem_chefe:
            total_violacoes += len(deps_sem_chefe)
            escrever_log(f"Foram encontrados {len(deps_sem_chefe)} departamentos sem chefe:")
            for dep in deps_sem_chefe:
                escrever_log(f"ID: {dep[0]}, Nome: {dep[1]}")
        else:
            escrever_log("OK -> Todos os departamentos possuem chefe atribuído")

        # 4. Todo professor deve ter departamento
        escrever_log("\nVALIDAÇÃO 4: Professores sem departamento")
        cursor.execute('''
            SELECT "Prof_ID", "Nome" 
            FROM "Professor" 
            WHERE "Departamento" IS NULL OR "Departamento" = '';
        ''')
        profs_sem_dep = cursor.fetchall()
        if profs_sem_dep:
            total_violacoes += len(profs_sem_dep)
            escrever_log(f"Foram encontrados {len(profs_sem_dep)} professores sem departamento:")
            for prof in profs_sem_dep:
                escrever_log(f"ID: {prof[0]}, Nome: {prof[1]}")
        else:
            escrever_log("OK -> Todos os professores possuem departamento atribuído")

        # 5. Toda disciplina deve ter departamento
        escrever_log("\nVALIDAÇÃO 5: Disciplinas sem departamento")
        cursor.execute('''
            SELECT "Disc_ID", "Nome" 
            FROM "Disciplina" 
            WHERE "Departamento" IS NULL OR "Departamento" = '';
        ''')
        discs_sem_dep = cursor.fetchall()
        if discs_sem_dep:
            total_violacoes += len(discs_sem_dep)
            escrever_log(f"Foram encontrados {len(discs_sem_dep)} disciplinas sem departamento:")
            for disc in discs_sem_dep:
                escrever_log(f"ID: {disc[0]}, Nome: {disc[1]}")
        else:
            escrever_log("OK -> Todas as disciplinas possuem departamento atribuído")

        # 6. Todo TCC deve ter orientador
        escrever_log("\nVALIDAÇÃO 6: TCCs sem orientador")
        cursor.execute('''
            SELECT "TCC_ID", "Titulo" 
            FROM "TCC" 
            WHERE "Orientador" IS NULL OR "Orientador" = '';
        ''')
        tccs_sem_orient = cursor.fetchall()
        if tccs_sem_orient:
            total_violacoes += len(tccs_sem_orient)
            escrever_log(f"Foram encontrados {len(tccs_sem_orient)} TCCs sem orientador:")
            for tcc in tccs_sem_orient:
                escrever_log(f"ID: {tcc[0]}, Título: {tcc[1]}")
        else:
            escrever_log("OK -> Todos os TCCs possuem orientador atribuído")

        # 7. Todo aluno deve estar no histórico
        escrever_log("\nVALIDAÇÃO 7: Alunos sem histórico")
        cursor.execute('''
            SELECT "RA", "Nome"
            FROM "Aluno"
            WHERE "RA" NOT IN (SELECT DISTINCT "RA" FROM "Historico_Aluno");
        ''')
        alunos_sem_hist = cursor.fetchall()
        if alunos_sem_hist:
            total_violacoes += len(alunos_sem_hist)
            escrever_log(f"Foram encontrados {len(alunos_sem_hist)} alunos sem histórico:")
            for aluno in alunos_sem_hist:
                escrever_log(f"RA: {aluno[0]}, Nome: {aluno[1]}")
        else:
            escrever_log("OK -> Todos os alunos possuem histórico")

        # 8. Todo professor deve estar no histórico
        escrever_log("\nVALIDAÇÃO 8: Professores sem histórico")
        cursor.execute('''
            SELECT "Prof_ID", "Nome"
            FROM "Professor"
            WHERE "Prof_ID" NOT IN (SELECT DISTINCT "Prof_ID" FROM "Historico_Professor");
        ''')
        profs_sem_hist = cursor.fetchall()
        if profs_sem_hist:
            total_violacoes += len(profs_sem_hist)
            escrever_log(f"Foram encontrados {len(profs_sem_hist)} professores sem histórico:")
            for prof in profs_sem_hist:
                escrever_log(f"ID: {prof[0]}, Nome: {prof[1]}")
        else:
            escrever_log("OK -> Todos os professores possuem histórico")

        # Resumo final
        escrever_log("\nRESUMO DA VALIDAÇÃO:")
        escrever_log(f"Total de violações encontradas: {total_violacoes}")
        if total_violacoes == 0:
            escrever_log("Todas as regras de validação foram atendidas!")
        else:
            escrever_log("Atenção, foram encontradas violações nas regras de validação!")

        escrever_log("\n" + "="*50)
        escrever_log("FIM DA VALIDAÇÃO")
        escrever_log("="*50 + "\n")

    except (Exception, Error) as error:
        escrever_log(f"erro ao validar: {error}")
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    validar_regras()