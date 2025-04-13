import random
import string
from faker import Faker
import psycopg2



fake = Faker('pt_BR')

# Função para gerar uma string aleatória
def gerar_string_aleatoria(tamanho, letras_ou_numeros='letras'):
    if letras_ou_numeros == 'letras':
        caracteres = string.ascii_letters  # Letras maiúsculas e minúsculas
    elif letras_ou_numeros == 'numeros':
        caracteres = string.digits  # Apenas números
    else:
        caracteres = string.ascii_letters + string.digits  # Letras e números

    return ''.join(random.choice(caracteres) for _ in range(tamanho))

###IDs

#RA_Aluno
IDS_Aluno = []
for i in range(1, 19):
    RA_Aluno = "A" + gerar_string_aleatoria(4, 'numeros')
    IDS_Aluno.append(RA_Aluno)




#Semestre Atual da tabela aluno
SAS_Aluno = []
for i in range(1, 11):
    SA_Aluno = random.randrange(2, 4)
    SAS_Aluno.append(SA_Aluno)
SA_Aluno11 = 1
SA_Aluno12 = 3
SA_Aluno13 = 4
SA_Aluno14 = 4
SA_Aluno15 = 4
SA_Aluno16 = 4
SA_Aluno17 = 4
SA_Aluno18 = 4
SAS_Aluno.append(SA_Aluno11)
SAS_Aluno.append(SA_Aluno12)
SAS_Aluno.append(SA_Aluno13)
SAS_Aluno.append(SA_Aluno14)
SAS_Aluno.append(SA_Aluno15)
SAS_Aluno.append(SA_Aluno16)
SAS_Aluno.append(SA_Aluno17)
SAS_Aluno.append(SA_Aluno18)


#Prof_ID
ID_Profs = []
#Gerar Profs de CC
ID_ProfsC = []
for i in range(1, 6):
    ID_Prof = "PC" + gerar_string_aleatoria(4, 'numeros')
    ID_Profs.append(ID_Prof)
    ID_ProfsC.append(ID_Prof)

#Gerar Profs de CD
ID_ProfsD = []
for i in range(1, 6):
    ID_Prof = "PD" + gerar_string_aleatoria(4, 'numeros')
    ID_Profs.append(ID_Prof)
    ID_ProfsD.append(ID_Prof)

#Gerar Profs de Física
ID_ProfsF = []
for i in range(1, 3):
    ID_Prof = "PF" + gerar_string_aleatoria(4, 'numeros')
    ID_Profs.append(ID_Prof)
    ID_ProfsF.append(ID_Prof)

#Gerar Profs de Matemática
ID_ProfsM = []
for i in range(1, 4):
    ID_Prof = "PM" + gerar_string_aleatoria(4, 'numeros')
    ID_Profs.append(ID_Prof)
    ID_ProfsM.append(ID_Prof)



#Dept_ID
ID_Depts = []

#Dept de Matemática

ID_Dept_CC = "DC" + gerar_string_aleatoria(2, 'numeros')

ID_Dept_CD = "DD" + gerar_string_aleatoria(2, 'numeros')

ID_Dept_Fis = "DF" + gerar_string_aleatoria(2, 'numeros')

ID_Dept_Mat = "DM" + gerar_string_aleatoria(2, 'numeros')

ID_Depts.append(ID_Dept_CC)
ID_Depts.append(ID_Dept_CD)
ID_Depts.append(ID_Dept_Fis)
ID_Depts.append(ID_Dept_Mat)


#Curso_ID
ID_Cursos = []
for i in range(1, 3):
    ID_Curso = "C" + gerar_string_aleatoria(2, 'numeros')
    ID_Cursos.append(ID_Curso)


#Disc_ID
IDS_Disc = []

#Gerar código para disciplina do dept de Ciências da Computação
for i in range(1, 11):
    ID_Disc = "CC" + gerar_string_aleatoria(4, 'numeros')
    IDS_Disc.append(ID_Disc)

for i in range(1, 11):
    ID_Disc = "CD" + gerar_string_aleatoria(4, 'numeros')
    IDS_Disc.append(ID_Disc)

#Gerar código para disciplina do dept de Física
for i in range(1, 3):
    ID_Disc = "F" + gerar_string_aleatoria(4, 'numeros')
    IDS_Disc.append(ID_Disc)

#Gerar código para disciplina do dept de Matemática
for i in range(1, 5):
    ID_Disc = "M" + gerar_string_aleatoria(4, 'numeros')
    IDS_Disc.append(ID_Disc)


#TCC_ID
ID_TCCs = []
for i in range(1, 3):
    ID_TCC = "T" + gerar_string_aleatoria(2, 'numeros')
    ID_TCCs.append(ID_TCC)





###Nomes

#Nome Aluno
Nomes_Aluno = []
for i in range(1, 19):
    Nome_Aluno = fake.name()
    Nomes_Aluno.append(Nome_Aluno)

#Nome Professor
Nomes_Prof = []
for i in range(1, 16):
    Nome_Prof = fake.name()
    Nomes_Prof.append(Nome_Prof)

#Nome Departamento
Nomes_Dept = []
Nome_Dept1 = "Ciências da Computação"
Nome_Dept2 = "Ciência de Dados"
Nome_Dept3 = "Fisica"
Nome_Dept4 = "Matemática"
Nomes_Dept.append(Nome_Dept1)
Nomes_Dept.append(Nome_Dept2)
Nomes_Dept.append(Nome_Dept3)
Nomes_Dept.append(Nome_Dept4)

#Nome Curso
Nomes_Curso = []
Nome_Curso1 = "Ciências da Computação"
Nome_Curso2 = "Ciência de Dados"
Nomes_Curso.append(Nome_Curso1)
Nomes_Curso.append(Nome_Curso2)

#Nome Disciplinas
Nomes_Disc = []
Nome_Disc1 = "Fundamentos de Algoritmos"
Nome_Disc2 = "Desenvolvimento Web"
Nome_Disc3 = "Desenvolvimento de Algoritmos"
Nome_Disc4 = "Sistemas Digitais"
Nome_Disc5 = "Orientação a Objetos"
Nome_Disc6 = "Redes de Computadores"
Nome_Disc7 = "Cálculo Numérico"
Nome_Disc8 = "Estrutura de Dados"
Nome_Disc9 = "Computação Móvel"
Nome_Disc10 = "Arquitetura de Computadores"
Nome_Disc11 = "Banco de Dados"
Nome_Disc12 = "Digital Experience"
Nome_Disc13 = "Digital Experience Ultimate"
Nome_Disc14 = "Fundamentos da Ciência e Visualização de Dados"
Nome_Disc15 = "Conectividade e IOT"
Nome_Disc16 = "Tratamento de Dados"
Nome_Disc17 = "Performance e Tunning de Dados"
Nome_Disc18 = "IA Clássica e Probabilística"
Nome_Disc19 = "Interação Humano-Computador"
Nome_Disc20 = "Aprendizado de Máquina"
Nome_Disc21 = "Física I"
Nome_Disc22 = "Física II"
Nome_Disc23 = "Cálculo I"
Nome_Disc24 = "Cálculo II"
Nome_Disc25 = "Cálculo III"
Nome_Disc26 = "Geometria Analítica"

Nomes_Disc.append(Nome_Disc1)
Nomes_Disc.append(Nome_Disc2)
Nomes_Disc.append(Nome_Disc3)
Nomes_Disc.append(Nome_Disc4)
Nomes_Disc.append(Nome_Disc5)
Nomes_Disc.append(Nome_Disc6)
Nomes_Disc.append(Nome_Disc7)
Nomes_Disc.append(Nome_Disc8)
Nomes_Disc.append(Nome_Disc9)
Nomes_Disc.append(Nome_Disc10)
Nomes_Disc.append(Nome_Disc11)
Nomes_Disc.append(Nome_Disc12)
Nomes_Disc.append(Nome_Disc13)
Nomes_Disc.append(Nome_Disc14)
Nomes_Disc.append(Nome_Disc15)
Nomes_Disc.append(Nome_Disc16)
Nomes_Disc.append(Nome_Disc17)
Nomes_Disc.append(Nome_Disc18)
Nomes_Disc.append(Nome_Disc19)
Nomes_Disc.append(Nome_Disc20)
Nomes_Disc.append(Nome_Disc21)
Nomes_Disc.append(Nome_Disc22)
Nomes_Disc.append(Nome_Disc23)
Nomes_Disc.append(Nome_Disc24)
Nomes_Disc.append(Nome_Disc25)
Nomes_Disc.append(Nome_Disc26)

#TCC_Títulos
TCC_Titulos = []
TCC_Titulo1 = "Localização de pessoas por Wi-Fi"
TCC_Titulo2 = "Análise de dados para otimização logística"
TCC_Titulos.append(TCC_Titulo1)
TCC_Titulos.append(TCC_Titulo2)

#Chefe Departamento
aux = random.randrange(0, len(ID_ProfsF))
Chefe_Dept_Fis = ID_ProfsF[aux]

aux = random.randrange(0, len(ID_ProfsM))
Chefe_Dept_Mat = ID_ProfsM[aux]

aux = random.randrange(0, len(ID_ProfsC))
Chefe_Dept_CC = ID_ProfsC[aux]

aux = random.randrange(0, len(ID_ProfsD))
Chefe_Dept_CD = ID_ProfsD[aux]

Chefes_Dept = []
Chefes_Dept.append(Chefe_Dept_CC)
Chefes_Dept.append(Chefe_Dept_CD)
Chefes_Dept.append(Chefe_Dept_Fis)
Chefes_Dept.append(Chefe_Dept_Mat)

#Coordenador de cada Curso
Curso_Cord = []
Curso_Cord1 = Chefe_Dept_CC
Curso_Cord2 = Chefe_Dept_CD
Curso_Cord.append(Curso_Cord1)
Curso_Cord.append(Curso_Cord2)

#Departamento de cada professor
Profs_Dept = []
for i in range(1, 6):
    Prof_Dept = ID_Dept_CC
    Profs_Dept.append(Prof_Dept)

for i in range(1, 6):
    Prof_Dept = ID_Dept_CD
    Profs_Dept.append(Prof_Dept)

for i in range(1, 3):
    Prof_Dept = ID_Dept_Fis
    Profs_Dept.append(Prof_Dept)

for i in range(1, 4):
    Prof_Dept = ID_Dept_Mat
    Profs_Dept.append(Prof_Dept)


# print(ID_Profs)
# print(Profs_Dept)

#Departamento das Disciplinas
Discs_Dept = []
for i in range(1, 11):
    Disc_Dept = ID_Dept_CC
    Discs_Dept.append(Disc_Dept)

for i in range(1, 11):
    Disc_Dept = ID_Dept_CD
    Discs_Dept.append(Disc_Dept)

for i in range(1, 3):
    Disc_Dept = ID_Dept_Fis
    Discs_Dept.append(Disc_Dept)

for i in range(1, 5):
    Disc_Dept = ID_Dept_Mat
    Discs_Dept.append(Disc_Dept)

#Orientadores dos TCCs
TCC_Orientadores = []
TCC_Orientador1 = Chefe_Dept_CC
TCC_Orientador2 = Chefe_Dept_CD
TCC_Orientadores.append(TCC_Orientador1)
TCC_Orientadores.append(TCC_Orientador2)

#Curso dos Alunos
Cursos_Alunos = []
for i in range(1, 11):
    aux = random.randrange(0, len(ID_Cursos))
    Curso_Alunos = ID_Cursos[aux]
    Cursos_Alunos.append(Curso_Alunos)

Cursos_Alunos.append(ID_Cursos[1])
Cursos_Alunos.append(ID_Cursos[1])
Cursos_Alunos.append(ID_Cursos[0])
Cursos_Alunos.append(ID_Cursos[0])
Cursos_Alunos.append(ID_Cursos[0])
Cursos_Alunos.append(ID_Cursos[1])
Cursos_Alunos.append(ID_Cursos[1])
Cursos_Alunos.append(ID_Cursos[1])

#print(Cursos_Alunos)

#Semestres da matriz curricular

Semestres_Matriz = [1, 1, 2, 3, 3, 3, 4, 4, 4, 4, 1, 2, 1, 2, 3, 2, 1, 1, 2, 3, 3, 3, 4, 4, 4, 4, 1, 2, 1, 2, 3, 2]

# print(len(IDS_Aluno))
# print(len(SAS_Aluno))

#Alunos com TCC
Alunos_TCC = []
for i in range(len(SAS_Aluno)):
    if SAS_Aluno[i] == 4:
        Alunos_TCC.append(IDS_Aluno[i])

#TCC de cada aluno
TCC_ID_Aluno = []
TCC_CC = []
TCC_CD = []
for i in range(len(Alunos_TCC)):
    if i < 3:
        TCC_ID_Aluno.append(ID_TCCs[0])
    else:
        TCC_ID_Aluno.append(ID_TCCs[1])

#Disciplinas de cada curso

Disc_CC = []
Disc_CD = []

for i in range(0, len(IDS_Disc)):
    if i < 10:
        Disc_CC.append(IDS_Disc[i])
    elif i >= 10 and i < 20:
        Disc_CD.append(IDS_Disc[i])
    else:
        Disc_CC.append(IDS_Disc[i])
        Disc_CD.append(IDS_Disc[i])

#Cursos de cada disciplina

Cursos_Disc = []
for i in range(0, 32):
    if i < 16:
        Cursos_Disc.append(ID_Cursos[0])
    else:
        Cursos_Disc.append(ID_Cursos[1])

#Index para matriz curricular
Index_Matriz = list(range(0, len(Cursos_Disc)))
#print(len(Index_Matriz))
#Anos de cada disciplina

Anos_Hist = []
for i in range(len(IDS_Aluno)):
    if SAS_Aluno[i] == 1:
        for j in range(0, 4):
            Anos_Hist.append("2025")
    if SAS_Aluno[i] == 2:
        for j in range(0,4):
            Anos_Hist.append("2024")
    if SAS_Aluno[i] == 3:
        for j in range(0, 8):
            Anos_Hist.append("2024")
    if SAS_Aluno[i] == 4:
        for j in range(0, 4):
            Anos_Hist.append("2023")
        for k in range(0, 8):
            Anos_Hist.append("2024")
    

#RA para histórico do aluno

RA_Hist = []
for i in range(len(IDS_Aluno)):
    if SAS_Aluno[i] == 1:
        for j in range(0, 4):
            RA_Hist.append(IDS_Aluno[i])
    elif SAS_Aluno[i] == 2:
        for j in range(0, 4):
            RA_Hist.append(IDS_Aluno[i])
    elif SAS_Aluno[i] == 3:
        for j in range(0, 8):
            RA_Hist.append(IDS_Aluno[i])
    elif SAS_Aluno[i] == 4:
        for j in range(0, 12):
            RA_Hist.append(IDS_Aluno[i])

#Disciplina para histórico do aluno

Disc_Hist = []
for i in range(len(IDS_Aluno)):
    if SAS_Aluno[i] == 1 and Cursos_Alunos[i] == ID_Cursos[0]:
        Disc_Hist.append(IDS_Disc[0])
        Disc_Hist.append(IDS_Disc[1])
        Disc_Hist.append(IDS_Disc[20])
        Disc_Hist.append(IDS_Disc[22])
    
    elif SAS_Aluno[i] == 1 and Cursos_Alunos[i] == ID_Cursos[1]:
        Disc_Hist.append(IDS_Disc[10])
        Disc_Hist.append(IDS_Disc[11])
        Disc_Hist.append(IDS_Disc[20])
        Disc_Hist.append(IDS_Disc[22])
    
    elif SAS_Aluno[i] == 2 and Cursos_Alunos[i] == ID_Cursos[0]:
        Disc_Hist.append(IDS_Disc[0])
        Disc_Hist.append(IDS_Disc[1])
        Disc_Hist.append(IDS_Disc[20])
        Disc_Hist.append(IDS_Disc[22])

    elif SAS_Aluno[i] == 2 and Cursos_Alunos[i] == ID_Cursos[1]:
        Disc_Hist.append(IDS_Disc[10])
        Disc_Hist.append(IDS_Disc[11])
        Disc_Hist.append(IDS_Disc[20])
        Disc_Hist.append(IDS_Disc[22])
   
    elif SAS_Aluno[i] == 3 and Cursos_Alunos[i] == ID_Cursos[0]:

        Disc_Hist.append(IDS_Disc[0])
        Disc_Hist.append(IDS_Disc[1])
        Disc_Hist.append(IDS_Disc[20])
        Disc_Hist.append(IDS_Disc[22])

        Disc_Hist.append(IDS_Disc[2])
        Disc_Hist.append(IDS_Disc[21])
        Disc_Hist.append(IDS_Disc[23])
        Disc_Hist.append(IDS_Disc[25])

    elif SAS_Aluno[i] == 3 and Cursos_Alunos[i] == ID_Cursos[1]:

        Disc_Hist.append(IDS_Disc[10])
        Disc_Hist.append(IDS_Disc[11])
        Disc_Hist.append(IDS_Disc[20])
        Disc_Hist.append(IDS_Disc[22])

        Disc_Hist.append(IDS_Disc[12])
        Disc_Hist.append(IDS_Disc[21])
        Disc_Hist.append(IDS_Disc[23])
        Disc_Hist.append(IDS_Disc[25])
    
    elif SAS_Aluno[i] == 4 and Cursos_Alunos[i] == ID_Cursos[0]:

        Disc_Hist.append(IDS_Disc[0])
        Disc_Hist.append(IDS_Disc[1])
        Disc_Hist.append(IDS_Disc[20])
        Disc_Hist.append(IDS_Disc[22])

        Disc_Hist.append(IDS_Disc[2])
        Disc_Hist.append(IDS_Disc[21])
        Disc_Hist.append(IDS_Disc[23])
        Disc_Hist.append(IDS_Disc[25])

        Disc_Hist.append(IDS_Disc[3])
        Disc_Hist.append(IDS_Disc[4])
        Disc_Hist.append(IDS_Disc[5])
        Disc_Hist.append(IDS_Disc[24])
    
    elif SAS_Aluno[i] == 4 and Cursos_Alunos[i] == ID_Cursos[1]:

        Disc_Hist.append(IDS_Disc[10])
        Disc_Hist.append(IDS_Disc[11])
        Disc_Hist.append(IDS_Disc[20])
        Disc_Hist.append(IDS_Disc[22])

        Disc_Hist.append(IDS_Disc[12])
        Disc_Hist.append(IDS_Disc[21])
        Disc_Hist.append(IDS_Disc[23])
        Disc_Hist.append(IDS_Disc[25])

        Disc_Hist.append(IDS_Disc[13])
        Disc_Hist.append(IDS_Disc[14])
        Disc_Hist.append(IDS_Disc[15])
        Disc_Hist.append(IDS_Disc[24])

#Nomes das disciplinas para histórico dos alunos
Nomes_Disc_Hist = []
for i in range(len(IDS_Aluno)):
    if SAS_Aluno[i] == 1 and Cursos_Alunos[i] == ID_Cursos[0]:
        Nomes_Disc_Hist.append(Nomes_Disc[0])
        Nomes_Disc_Hist.append(Nomes_Disc[1])
        Nomes_Disc_Hist.append(Nomes_Disc[20])
        Nomes_Disc_Hist.append(Nomes_Disc[22])
    
    elif SAS_Aluno[i] == 1 and Cursos_Alunos[i] == ID_Cursos[1]:
        Nomes_Disc_Hist.append(Nomes_Disc[10])
        Nomes_Disc_Hist.append(Nomes_Disc[11])
        Nomes_Disc_Hist.append(Nomes_Disc[20])
        Nomes_Disc_Hist.append(Nomes_Disc[22])
    
    elif SAS_Aluno[i] == 2 and Cursos_Alunos[i] == ID_Cursos[0]:
        Nomes_Disc_Hist.append(Nomes_Disc[0])
        Nomes_Disc_Hist.append(Nomes_Disc[1])
        Nomes_Disc_Hist.append(Nomes_Disc[20])
        Nomes_Disc_Hist.append(Nomes_Disc[22])

    elif SAS_Aluno[i] == 2 and Cursos_Alunos[i] == ID_Cursos[1]:
        Nomes_Disc_Hist.append(Nomes_Disc[10])
        Nomes_Disc_Hist.append(Nomes_Disc[11])
        Nomes_Disc_Hist.append(Nomes_Disc[20])
        Nomes_Disc_Hist.append(Nomes_Disc[22])
   
    elif SAS_Aluno[i] == 3 and Cursos_Alunos[i] == ID_Cursos[0]:

        Nomes_Disc_Hist.append(Nomes_Disc[0])
        Nomes_Disc_Hist.append(Nomes_Disc[1])
        Nomes_Disc_Hist.append(Nomes_Disc[20])
        Nomes_Disc_Hist.append(Nomes_Disc[22])

        Nomes_Disc_Hist.append(Nomes_Disc[2])
        Nomes_Disc_Hist.append(Nomes_Disc[21])
        Nomes_Disc_Hist.append(Nomes_Disc[23])
        Nomes_Disc_Hist.append(Nomes_Disc[25])

    elif SAS_Aluno[i] == 3 and Cursos_Alunos[i] == ID_Cursos[1]:

        Nomes_Disc_Hist.append(Nomes_Disc[10])
        Nomes_Disc_Hist.append(Nomes_Disc[11])
        Nomes_Disc_Hist.append(Nomes_Disc[20])
        Nomes_Disc_Hist.append(Nomes_Disc[22])

        Nomes_Disc_Hist.append(Nomes_Disc[12])
        Nomes_Disc_Hist.append(Nomes_Disc[21])
        Nomes_Disc_Hist.append(Nomes_Disc[23])
        Nomes_Disc_Hist.append(Nomes_Disc[25])
    
    elif SAS_Aluno[i] == 4 and Cursos_Alunos[i] == ID_Cursos[0]:

        Nomes_Disc_Hist.append(Nomes_Disc[0])
        Nomes_Disc_Hist.append(Nomes_Disc[1])
        Nomes_Disc_Hist.append(Nomes_Disc[20])
        Nomes_Disc_Hist.append(Nomes_Disc[22])

        Nomes_Disc_Hist.append(Nomes_Disc[2])
        Nomes_Disc_Hist.append(Nomes_Disc[21])
        Nomes_Disc_Hist.append(Nomes_Disc[23])
        Nomes_Disc_Hist.append(Nomes_Disc[25])

        Nomes_Disc_Hist.append(Nomes_Disc[3])
        Nomes_Disc_Hist.append(Nomes_Disc[4])
        Nomes_Disc_Hist.append(Nomes_Disc[5])
        Nomes_Disc_Hist.append(Nomes_Disc[24])
    
    elif SAS_Aluno[i] == 4 and Cursos_Alunos[i] == ID_Cursos[1]:

        Nomes_Disc_Hist.append(Nomes_Disc[10])
        Nomes_Disc_Hist.append(Nomes_Disc[11])
        Nomes_Disc_Hist.append(Nomes_Disc[20])
        Nomes_Disc_Hist.append(Nomes_Disc[22])

        Nomes_Disc_Hist.append(Nomes_Disc[12])
        Nomes_Disc_Hist.append(Nomes_Disc[21])
        Nomes_Disc_Hist.append(Nomes_Disc[23])
        Nomes_Disc_Hist.append(Nomes_Disc[25])

        Nomes_Disc_Hist.append(Nomes_Disc[13])
        Nomes_Disc_Hist.append(Nomes_Disc[14])
        Nomes_Disc_Hist.append(Nomes_Disc[15])
        Nomes_Disc_Hist.append(Nomes_Disc[24])


#Aprovação para o histórico
Aprov_Hist = []
for i in range(len(IDS_Aluno)):
    if SAS_Aluno[i] == 1:
        for j in range(0, 4):
            Aprov_Hist.append(None)
    elif SAS_Aluno[i] == 2:
        for j in range(0, 4):
            Aprov_Hist.append("Aprovado")
    elif SAS_Aluno[i] == 3:
        for j in range(0, 8):
            Aprov_Hist.append("Aprovado")
    elif SAS_Aluno[i] == 4:
        for j in range(0, 12):
            Aprov_Hist.append("Aprovado")

#Semestres para o histórico
Sem_Hist = []
for i in range(len(IDS_Aluno)):
    if SAS_Aluno[i] == 1:
        for j in range(0, 4):
            Sem_Hist.append("Primeiro")
    elif SAS_Aluno[i] == 2:
        for j in range(0, 4):
            Sem_Hist.append("Segundo")
    elif SAS_Aluno[i] == 3:
        for j in range(0, 4):
            Sem_Hist.append("Primeiro")
        for k in range(0, 4):
            Sem_Hist.append("Segundo")
    elif SAS_Aluno[i] == 4:
        for j in range(0, 4):
            Sem_Hist.append("Segundo")
        for k in range(0, 4):
            Sem_Hist.append("Primeiro")
        for l in range(0, 4):
            Sem_Hist.append("Segundo")

#Index histórico
Index_Hist = list(range(0, len(RA_Hist)))

# print(len(Anos_Hist))
# print(len(RA_Hist))
# print(len(Disc_Hist))
# print(len(Aprov_Hist))
# print(len(Sem_Hist))
# print(len(Index_Hist))

#Histórico Professor

#Prof_ID para o histórico de professores
Prof_ID_Hist = []
for i in range(len(ID_ProfsC)):
    for j in range(0, 2):
        Prof_ID_Hist.append(ID_ProfsC[i])

for i in range(len(ID_ProfsD)):
    for j in range(0, 2):
        Prof_ID_Hist.append(ID_ProfsD[i])

for i in range(len(ID_ProfsF)):
    Prof_ID_Hist.append(ID_ProfsF[i])

for i in range(len(ID_ProfsM)):
    if i == 0:
        Prof_ID_Hist.append(ID_ProfsM[i])
        Prof_ID_Hist.append(ID_ProfsM[i])
    else:
        Prof_ID_Hist.append(ID_ProfsM[i])

for i in range(len(ID_ProfsC)):
    for j in range(0, 2):
        Prof_ID_Hist.append(ID_ProfsC[i])

for i in range(len(ID_ProfsD)):
    for j in range(0, 2):
        Prof_ID_Hist.append(ID_ProfsD[i])

for i in range(len(ID_ProfsF)):
    Prof_ID_Hist.append(ID_ProfsF[i])

for i in range(len(ID_ProfsM)):
    if i == 0:
        Prof_ID_Hist.append(ID_ProfsM[i])
        Prof_ID_Hist.append(ID_ProfsM[i])
    else:
        Prof_ID_Hist.append(ID_ProfsM[i])

for i in range(len(ID_ProfsC)):
    for j in range(0, 2):
        Prof_ID_Hist.append(ID_ProfsC[i])

for i in range(len(ID_ProfsD)):
    for j in range(0, 2):
        Prof_ID_Hist.append(ID_ProfsD[i])

for i in range(len(ID_ProfsF)):
    Prof_ID_Hist.append(ID_ProfsF[i])

for i in range(len(ID_ProfsM)):
    if i == 0:
        Prof_ID_Hist.append(ID_ProfsM[i])
        Prof_ID_Hist.append(ID_ProfsM[i])
    else:
        Prof_ID_Hist.append(ID_ProfsM[i])

for i in range(len(ID_ProfsC)):
    for j in range(0, 2):
        Prof_ID_Hist.append(ID_ProfsC[i])

for i in range(len(ID_ProfsD)):
    for j in range(0, 2):
        Prof_ID_Hist.append(ID_ProfsD[i])

for i in range(len(ID_ProfsF)):
    Prof_ID_Hist.append(ID_ProfsF[i])

for i in range(len(ID_ProfsM)):
    if i == 0:
        Prof_ID_Hist.append(ID_ProfsM[i])
        Prof_ID_Hist.append(ID_ProfsM[i])
    else:
        Prof_ID_Hist.append(ID_ProfsM[i])

#Disciplinas para o histórico de professores

Disc_Hist_Prof = []
for i in range(0, 4):
    for i in range(len(IDS_Disc)):
        Disc_Hist_Prof.append(IDS_Disc[i])






#Semestre para o histórico de professores
Sem_Hist_Prof = []
for i in range(0, 26):
    Sem_Hist_Prof.append("Primeiro")
for i in range(0, 26):
    Sem_Hist_Prof.append("Segundo")
for i in range(0, 26):
    Sem_Hist_Prof.append("Primeiro")
for i in range(0, 26):
    Sem_Hist_Prof.append("Segundo")


#Ano para o histórico de professores
Anos_Hist_Prof = []
for i in range(0, 26):
    Anos_Hist_Prof.append("2025")
for i in range(0, 52):
    Anos_Hist_Prof.append("2024")
for i in range(0, 26):
    Anos_Hist_Prof.append("2023")


#Index para o histórico de professores
Index_Hist_Prof = list(range(0, len(Prof_ID_Hist)))

# print(Disc_Hist_Prof)
# print(len(Disc_Hist_Prof))
# print(len(Prof_ID_Hist))
# print(len(Sem_Hist_Prof))
# print(len(Anos_Hist_Prof))
# print(len(Index_Hist_Prof))

#Aluno com reprovação
RA_Reprov = []
Nome_Reprov = []
Curso_Reprov = []
Sem_Reprov = []
RA_Reprov.append("A" + gerar_string_aleatoria(4, 'numeros'))
Nome_Reprov.append(fake.name())
Curso_Reprov.append(ID_Cursos[0])
Sem_Reprov.append(3)

#Histórico do aluno com reprovação
RA_Reprov_Hist = []
Disc_Reprov_Hist = []
Nome_Disc_Reprov_Hist = []
Sem_Reprov_Hist = []
Anos_Reprov_Hist = []
Aprov_Reprov_Hist = []
Index_Reprov_Hist = list(range(len(Index_Hist), len(Index_Hist) + 9))

for i in range(0, 9):
    RA_Reprov_Hist.append(RA_Reprov[0])

Disc_Reprov_Hist.append(IDS_Disc[0])
Disc_Reprov_Hist.append(IDS_Disc[1])
Disc_Reprov_Hist.append(IDS_Disc[20])
Disc_Reprov_Hist.append(IDS_Disc[22])
Disc_Reprov_Hist.append(IDS_Disc[2])
Disc_Reprov_Hist.append(IDS_Disc[21])
Disc_Reprov_Hist.append(IDS_Disc[23])
Disc_Reprov_Hist.append(IDS_Disc[25])
Disc_Reprov_Hist.append(IDS_Disc[0])

Nome_Disc_Reprov_Hist.append(Nomes_Disc[0])
Nome_Disc_Reprov_Hist.append(Nomes_Disc[1])
Nome_Disc_Reprov_Hist.append(Nomes_Disc[20])
Nome_Disc_Reprov_Hist.append(Nomes_Disc[22])
Nome_Disc_Reprov_Hist.append(Nomes_Disc[2])
Nome_Disc_Reprov_Hist.append(Nomes_Disc[21])
Nome_Disc_Reprov_Hist.append(Nomes_Disc[23])
Nome_Disc_Reprov_Hist.append(Nomes_Disc[25])
Nome_Disc_Reprov_Hist.append(Nomes_Disc[0])

for i in range(0, 4):
    Sem_Reprov_Hist.append("Primeiro")
for i in range(0, 5):
    Sem_Reprov_Hist.append("Segundo")

for i in range(0, 9):
    Anos_Reprov_Hist.append("2024")

Aprov_Reprov_Hist.append("Reprovado")
for i in range(0, 8):
    Aprov_Reprov_Hist.append("Aprovado")

# print(Aprov_Reprov_Hist)

#Professor com disciplina lecionada anteriormente
ID_Prof_Lec = []
Nome_Prof_Lec = []


ID_Prof_Lec.append("PC" + gerar_string_aleatoria(4, 'numeros'))
Nome_Prof_Lec.append(fake.name())
Dept_Lec = ID_Dept_CC



#Histórico do professor com disciplina lecionada anteriormente
ID_Prof_Lec_Hist = []
ID_Disc_Lec_Hist = []
Sem_Lec = []
Ano_Lec = []

for i in range(0, 2):
    ID_Prof_Lec_Hist.append(ID_Prof_Lec[0])

ID_Disc_Lec_Hist.append(IDS_Disc[0])
ID_Disc_Lec_Hist.append(IDS_Disc[1])
Ano_Lec.append("2024")
Ano_Lec.append("2025")
Sem_Lec.append("Segundo")
Sem_Lec.append("Primeiro")
Index_Lec = list(range(len(Index_Hist_Prof),len(Index_Hist_Prof) + 2))

# print(len(RA_Reprov_Hist))
# print(len(Disc_Reprov_Hist))
# print(len(Sem_Reprov_Hist))
# print(len(Anos_Reprov_Hist))
# print(len(Aprov_Reprov_Hist))
# print(len(Index_Reprov_Hist))

# print(len(Disc_CC))
# print(len(Disc_CD))
# print(len(Cursos_Disc))

# print(len(Prof_ID_Hist))
# print(len(IDS_Disc))
# print(len(Sem_Hist_Prof))
# print(len(Anos_Hist_Prof))
# print(len(Index_Hist_Prof))

# try:
#     conexao = psycopg2.connect(
#         dbname='postgres',
#         user='postgres',
#         password='Foguete50',
#         host='db.muxslmzihfxhaawvvtne.supabase.co',
#         port='5432'
#     )
#     cursor = conexao.cursor()
#     cursor.execute("SELECT 1;")
#     resultado = cursor.fetchone()
#     print("Conexão bem-sucedida. Resultado do teste:", resultado)
# except Exception as ex:
#     print("Falha na conexão:", ex)
# finally:
#     if 'cursor' in locals():
#         cursor.close()
#     if 'conexao' in locals():
#         conexao.close()

# Template para apagar dados de tabela caso necessário
# try:
#     conexao = psycopg2.connect(
#         user="postgres.plfcanmzyxajqkpqyiov",
#         password="Foguete50",
#         host="aws-0-sa-east-1.pooler.supabase.com",
#         port="5432",
#         dbname="postgres",
#     )
#     cursor = conexao.cursor()

#     sql_delete = """
#     DELETE FROM "Professor";
#     """
#     cursor.execute(sql_delete)
#     conexao.commit() 

#     print("Todos os dados da tabela foram excluídos com sucesso!")

# except Exception as ex:
#     print("Erro ao inserir dados:", ex)
# finally:
#     if 'cursor' in locals():
#         cursor.close()
#     if 'conexao' in locals():
#         conexao.close()


if __name__ == '__main__':
    try:
        # Conecta uma única vez
        print("Conectando ao banco de dados...")
        conexao = psycopg2.connect(
            user="postgres.plfcanmzyxajqkpqyiov",
            password="Foguete50",
            host="aws-0-sa-east-1.pooler.supabase.com",
            port="5432",
            dbname="postgres",
        )
        cursor = conexao.cursor()
        print("Conexão estabelecida com sucesso!")

        # 1. Insere Cursos
        print("\nInserindo cursos...")
        for i in range(len(ID_Cursos)):
            cursor.execute("""
                INSERT INTO "Curso" ("Curso_ID", "Nome")
                VALUES (%s, %s)
                """, (ID_Cursos[i], Nomes_Curso[i]))
        print(f"{len(ID_Cursos)} cursos inseridos com sucesso!")

        # 2. Insere Departamentos
        print("\nInserindo departamentos...")
        for i in range(len(ID_Depts)):
            cursor.execute("""
                INSERT INTO "Departamento" ("Dept_ID", "Nome")
                VALUES (%s, %s)
                """, (ID_Depts[i], Nomes_Dept[i]))
        print(f"{len(ID_Depts)} departamentos inseridos com sucesso!")

        # 3. Insere Professores
        print("\nInserindo professores...")
        for i in range(len(ID_Profs)):
            cursor.execute("""
                INSERT INTO "Professor" ("Prof_ID", "Nome", "Departamento")
                VALUES (%s, %s, %s)
                """, (ID_Profs[i], Nomes_Prof[i], Profs_Dept[i]))
        print(f"{len(ID_Profs)} professores inseridos com sucesso!")

        # 4. Atualiza Chefes de Departamento
        print("\nAtualizando chefes de departamento...")
        for i in range(len(Chefes_Dept)):
            cursor.execute("""
                UPDATE "Departamento"
                SET "Chefe" = %s
                WHERE "Dept_ID" = %s
                """, (Chefes_Dept[i], ID_Depts[i]))
        print(f"{len(Chefes_Dept)} chefes de departamento atualizados com sucesso!")

        # 5. Atualiza Coordenadores de Curso
        print("\nAtualizando coordenadores de curso...")
        for i in range(len(Curso_Cord)):
            cursor.execute("""
                UPDATE "Curso"
                SET "Coordenador" = %s
                WHERE "Curso_ID" = %s
                """, (Curso_Cord[i], ID_Cursos[i]))
        print(f"{len(Curso_Cord)} coordenadores de curso atualizados com sucesso!")

        # 6. Insere Disciplinas (com tratamento para nomes duplicados)
        print("\nInserindo disciplinas...")
        disciplinas_inseridas = 0
        for i in range(len(IDS_Disc)):
            try:
                cursor.execute("""
                    INSERT INTO "Disciplina" ("Disc_ID", "Nome", "Departamento")
                    VALUES (%s, %s, %s)
                    ON CONFLICT ("Nome") DO NOTHING
                    """, (IDS_Disc[i], Nomes_Disc[i], Discs_Dept[i]))
                if cursor.rowcount > 0:
                    disciplinas_inseridas += 1
            except IntegrityError as e:
                print(f"  Aviso: Disciplina '{Nomes_Disc[i]}' já existe, pulando...")
                continue
        print(f"{disciplinas_inseridas} disciplinas inseridas com sucesso!")

        # 7. Insere Alunos
        print("\nInserindo alunos...")
        for i in range(len(IDS_Aluno)):
            cursor.execute("""
                INSERT INTO "Aluno" ("RA", "Nome", "Curso", "Semestre_Atual")
                VALUES (%s, %s, %s, %s)
                """, (IDS_Aluno[i], Nomes_Aluno[i], Cursos_Alunos[i], SAS_Aluno[i]))
        print(f"{len(IDS_Aluno)} alunos inseridos com sucesso!")

        # 8. Insere TCCs
        print("\nInserindo TCCs...")
        for i in range(len(ID_TCCs)):
            cursor.execute("""
                INSERT INTO "TCC" ("TCC_ID", "Titulo", "Orientador")
                VALUES (%s, %s, %s)
                """, (ID_TCCs[i], TCC_Titulos[i], TCC_Orientadores[i]))
        print(f"{len(ID_TCCs)} TCCs inseridos com sucesso!")

        # 9. Insere TCC_Aluno
        print("\nVinculando alunos a TCCs...")
        for i in range(len(Alunos_TCC)):
            cursor.execute("""
                INSERT INTO "TCC_Aluno" ("RA", "TCC_ID")
                VALUES (%s, %s)
                """, (Alunos_TCC[i], TCC_ID_Aluno[i]))
        print(f"{len(Alunos_TCC)} vínculos aluno-TCC criados com sucesso!")

        # 10. Insere Matriz Curricular
        print("\nInserindo matriz curricular...")
        for i in range(len(Cursos_Disc)):
            disc = Disc_CC[i] if i < 16 else Disc_CD[i - 16]
            cursor.execute("""
                INSERT INTO "Matriz_Curricular" ("Curso_ID", "Disc_ID", "Semestre", "Index")
                VALUES (%s, %s, %s, %s)
                """, (Cursos_Disc[i], disc, Semestres_Matriz[i], Index_Matriz[i]))
        print(f"{len(Cursos_Disc)} itens da matriz curricular inseridos com sucesso!")

        # 11. Insere Histórico de Alunos
        print("\nInserindo histórico de alunos...")
        for i in range(len(RA_Hist)):
            cursor.execute("""
                INSERT INTO "Historico_Aluno" ("RA", "Disc_ID", "Index", "Disc_Nome", "Semestre", "Ano", "Aprovacao")
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (RA_Hist[i], Disc_Hist[i], Index_Hist[i], Nomes_Disc_Hist[i], 
                     Sem_Hist[i], Anos_Hist[i], Aprov_Hist[i]))
        print(f"{len(RA_Hist)} registros de histórico de alunos inseridos com sucesso!")

        # 12. Insere Histórico de Professores
        print("\nInserindo histórico de professores...")
        for i in range(len(Prof_ID_Hist)):
            cursor.execute("""
                INSERT INTO "Historico_Professor" ("Prof_ID", "Disc_ID", "Semestre", "Ano", "Index")
                VALUES (%s, %s, %s, %s, %s)
                """, (Prof_ID_Hist[i], Disc_Hist_Prof[i], Sem_Hist_Prof[i], 
                     Anos_Hist_Prof[i], Index_Hist_Prof[i]))
        print(f"{len(Prof_ID_Hist)} registros de histórico de professores inseridos com sucesso!")

        # 13. Insere Aluno Especial (com reprovação)
        print("\nInserindo aluno especial (com reprovação)...")
        cursor.execute("""
            INSERT INTO "Aluno" ("RA", "Nome", "Curso", "Semestre_Atual")
            VALUES (%s, %s, %s, %s)
            """, (RA_Reprov[0], Nome_Reprov[0], Curso_Reprov[0], Sem_Reprov[0]))
        print("Aluno especial inserido com sucesso!")

        # 14. Insere Histórico do Aluno Especial
        print("\nInserindo histórico do aluno especial...")
        for i in range(len(RA_Reprov_Hist)):
            cursor.execute("""
                INSERT INTO "Historico_Aluno" ("RA", "Disc_ID", "Index", "Disc_Nome", "Semestre", "Ano", "Aprovacao")
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (RA_Reprov_Hist[i], Disc_Reprov_Hist[i], Index_Reprov_Hist[i],
                     Nome_Disc_Reprov_Hist[i], Sem_Reprov_Hist[i], Anos_Reprov_Hist[i],
                     Aprov_Reprov_Hist[i]))
        print(f"{len(RA_Reprov_Hist)} registros de histórico do aluno especial inseridos com sucesso!")

        # 15. Insere Professor Especial
        print("\nInserindo professor especial...")
        cursor.execute("""
            INSERT INTO "Professor" ("Prof_ID", "Nome", "Departamento")
            VALUES (%s, %s, %s)
            """, (ID_Prof_Lec[0], Nome_Prof_Lec[0], Dept_Lec))
        print("Professor especial inserido com sucesso!")

        # 16. Insere Histórico do Professor Especial
        print("\nInserindo histórico do professor especial...")
        for i in range(len(ID_Prof_Lec_Hist)):
            cursor.execute("""
                INSERT INTO "Historico_Professor" ("Prof_ID", "Disc_ID", "Semestre", "Ano", "Index")
                VALUES (%s, %s, %s, %s, %s)
                """, (ID_Prof_Lec_Hist[i], ID_Disc_Lec_Hist[i], Sem_Lec[i],
                     Ano_Lec[i], Index_Lec[i]))
        print(f"{len(ID_Prof_Lec_Hist)} registros de histórico do professor especial inseridos com sucesso!")

        # Commit final para todas as operações
        conexao.commit()
        print("\nOperações concluídas com sucesso! Todos os dados foram inseridos.")

    except Exception as ex:
        print("\nErro durante as operações:", ex)
        if 'conexao' in locals():
            conexao.rollback()
        print("Todas as operações foram revertidas devido ao erro.")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()
            print("\nConexão com o banco de dados encerrada.")
