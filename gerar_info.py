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

#Semestre para o histórico de professores
Sem_Hist_Prof = []
for i in range(0, 26):
    Sem_Hist_Prof.append("Primeiro")

#Ano para o histórico de professores
Anos_Hist_Prof = []
for i in range(0, 26):
    Anos_Hist_Prof.append("2025")

#Index para o histórico de professores
Index_Hist_Prof = list(range(0, len(Prof_ID_Hist)))

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

print(Aprov_Reprov_Hist)

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

if __name__ == '__main__':
	try:
		conexao = psycopg2.connect(
			user="postgres.muxslmzihfxhaawvvtne" ,
			password="Foguete50",
			host="aws-0-sa-east-1.pooler.supabase.com",
			port="6543",
			dbname="postgres",
		)
		cursor = conexao.cursor()
		cursor.execute("SELECT 1;")
		resultado = cursor.fetchone()
		print("Conexão bem-sucedida. Resultado do teste:", resultado)
	except Exception as ex:
		print("Falha na conexão:", ex)
	finally:
		if 'cursor' in locals():
			cursor.close()
		if 'conexao' in locals():
			conexao.close()

# Template para apagar dados de tabela caso necessário
# try:
#     conexao = psycopg2.connect(
#         user="postgres.muxslmzihfxhaawvvtne",
#         password="Foguete50",
#         host="aws-0-sa-east-1.pooler.supabase.com",
#         port="6543",
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



try:
    conexao = psycopg2.connect(
        user="postgres.muxslmzihfxhaawvvtne",
        password="Foguete50",
        host="aws-0-sa-east-1.pooler.supabase.com",
        port="6543",
        dbname="postgres",
    )
    cursor = conexao.cursor()

    for i in range(len(ID_Cursos)):
        ID_Curso = ID_Cursos[i]
        Nome_Curso = Nomes_Curso[i]

        sql_insert = """
        INSERT INTO "Curso" ("Curso_ID", "Nome")
        VALUES (%s, %s)
        """
        cursor.execute(sql_insert, (ID_Curso, Nome_Curso))
        
    conexao.commit()
    print(f"{len(ID_Cursos)} cursos inseridos com sucesso!")

except Exception as ex:
    print("Erro ao inserir dados:", ex)
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conexao' in locals():
        conexao.close()

try:
    conexao = psycopg2.connect(
        user="postgres.muxslmzihfxhaawvvtne",
        password="Foguete50",
        host="aws-0-sa-east-1.pooler.supabase.com",
        port="6543",
        dbname="postgres",
    )
    cursor = conexao.cursor()

    for i in range(len(IDS_Aluno)):
        RA_Aluno = IDS_Aluno[i]
        Nome_Aluno = Nomes_Aluno[i]
        Curso_Aluno = Cursos_Alunos[i]
        Semestre_Atual = SAS_Aluno[i]

        # Comando SQL para inserir dados
        sql_insert = """
        INSERT INTO "Aluno" ("RA", "Nome", "Curso", "Semestre_Atual")
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql_insert, (RA_Aluno, Nome_Aluno, Curso_Aluno, Semestre_Atual))
    
    conexao.commit()
    print(f"{len(IDS_Aluno)} alunos inseridos com sucesso!")

except Exception as ex:
    print("Erro ao inserir dados:", ex)
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conexao' in locals():
        conexao.close()

try:
    conexao = psycopg2.connect(
        user="postgres.muxslmzihfxhaawvvtne",
        password="Foguete50",
        host="aws-0-sa-east-1.pooler.supabase.com",
        port="6543",
        dbname="postgres",
    )
    cursor = conexao.cursor()

    for i in range(len(ID_Depts)):
        ID_Dept = ID_Depts[i]
        Nome_Dept = Nomes_Dept[i]

        # Comando SQL para inserir dados
        sql_insert = """
        INSERT INTO "Departamento" ("Dept_ID", "Nome")
        VALUES (%s, %s)
        """
        cursor.execute(sql_insert, (ID_Dept, Nome_Dept))
    
    conexao.commit()
    print(f"{len(ID_Depts)} departamentos inseridos com sucesso!")

except Exception as ex:
    print("Erro ao inserir dados:", ex)
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conexao' in locals():
        conexao.close()

try:
    conexao = psycopg2.connect(
        user="postgres.muxslmzihfxhaawvvtne",
        password="Foguete50",
        host="aws-0-sa-east-1.pooler.supabase.com",
        port="6543",
        dbname="postgres",
    )
    cursor = conexao.cursor()

    for i in range(len(ID_Profs)):
        Prof_ID = ID_Profs[i]
        Nome_Prof = Nomes_Prof[i]
        Prof_Dept = Profs_Dept[i]

        # Comando SQL para inserir dados
        sql_insert = """
        INSERT INTO "Professor" ("Prof_ID", "Nome", "Departamento")
        VALUES (%s, %s, %s)
        """
        cursor.execute(sql_insert, (Prof_ID, Nome_Prof, Prof_Dept))
    
    conexao.commit()
    
    for i in range(len(Chefes_Dept)):
        Chefe_Dept = Chefes_Dept[i]
        ID_Dept = ID_Depts[i]

        sql_update_dept = """
        UPDATE "Departamento"
        SET "Chefe" = %s
        WHERE "Dept_ID" = %s
        """

        cursor.execute(sql_update_dept, (Chefe_Dept, ID_Dept))
    
    conexao.commit()

    
    for i in range(len(ID_Cursos)):
        Cord_Curso = Curso_Cord[i]
        ID_Curso = ID_Cursos[i]

        sql_update_curso = """
        UPDATE "Curso"
        SET "Coordenador" = %s
        WHERE "Curso_ID" = %s
        """

        cursor.execute(sql_update_curso, (Cord_Curso, ID_Curso))

    conexao.commit()
    print(f"{len(ID_Profs)} professores inseridos com sucesso!")


except Exception as ex:
    print("Erro ao inserir dados:", ex)
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conexao' in locals():
        conexao.close()

try:
    conexao = psycopg2.connect(
        user="postgres.muxslmzihfxhaawvvtne",
        password="Foguete50",
        host="aws-0-sa-east-1.pooler.supabase.com",
        port="6543",
        dbname="postgres",
    )
    cursor = conexao.cursor()

    for i in range(len(IDS_Disc)):
        ID_Disc = IDS_Disc[i]
        Nome_Disc = Nomes_Disc[i]
        Disc_Dept = Discs_Dept[i]

        # Comando SQL para inserir dados
        sql_insert = """
        INSERT INTO "Disciplina" ("Disc_ID", "Nome", "Departamento")
        VALUES (%s, %s, %s)
        """
        cursor.execute(sql_insert, (ID_Disc, Nome_Disc, Disc_Dept))
    
    conexao.commit()
    print(f"{len(IDS_Disc)} disciplinas inseridos com sucesso!")

except Exception as ex:
    print("Erro ao inserir dados:", ex)
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conexao' in locals():
        conexao.close()

try:
    conexao = psycopg2.connect(
        user="postgres.muxslmzihfxhaawvvtne",
        password="Foguete50",
        host="aws-0-sa-east-1.pooler.supabase.com",
        port="6543",
        dbname="postgres",
    )
    cursor = conexao.cursor()

    for i in range(len(ID_TCCs)):
        ID_TCC = ID_TCCs[i]
        Titulo_TCC = TCC_Titulos[i]
        Orientador_TCC = TCC_Orientadores[i]

        # Comando SQL para inserir dados
        sql_insert = """
        INSERT INTO "TCC" ("TCC_ID", "Titulo", "Orientador")
        VALUES (%s, %s, %s)
        """
        cursor.execute(sql_insert, (ID_TCC, Titulo_TCC, Orientador_TCC))
    
    conexao.commit()
    print(f"{len(ID_TCCs)} TCCs inseridos com sucesso!")

except Exception as ex:
    print("Erro ao inserir dados:", ex)
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conexao' in locals():
        conexao.close()

try:
    conexao = psycopg2.connect(
        user="postgres.muxslmzihfxhaawvvtne",
        password="Foguete50",
        host="aws-0-sa-east-1.pooler.supabase.com",
        port="6543",
        dbname="postgres",
    )
    cursor = conexao.cursor()

    for i in range(len(Alunos_TCC)):
        RA_TCC = Alunos_TCC[i]
        TCC_ID = TCC_ID_Aluno[i]

        # Comando SQL para inserir dados
        sql_insert = """
        INSERT INTO "TCC_Aluno" ("RA", "TCC_ID")
        VALUES (%s, %s)
        """
        cursor.execute(sql_insert, (RA_TCC, TCC_ID))
    
    conexao.commit()
    print(f"{len(Alunos_TCC)} TCCs de alunos inseridos com sucesso!")

except Exception as ex:
    print("Erro ao inserir dados:", ex)
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conexao' in locals():
        conexao.close()

try:
    conexao = psycopg2.connect(
        user="postgres.muxslmzihfxhaawvvtne",
        password="Foguete50",
        host="aws-0-sa-east-1.pooler.supabase.com",
        port="6543",
        dbname="postgres",
    )
    cursor = conexao.cursor()

    for i in range(len(Cursos_Disc)):
        Curso_Disc = Cursos_Disc[i]
        if i < 16:
            Disc = Disc_CC[i]
        else:
            Disc = Disc_CD[i - 16]
        Sem_Matriz = Semestres_Matriz[i]
        Index = Index_Matriz[i]


        # Comando SQL para inserir dados
        sql_insert = """
        INSERT INTO "Matriz_Curricular" ("Curso_ID", "Disc_ID", "Semestre", "Index")
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql_insert, (Curso_Disc, Disc, Sem_Matriz, Index))
    
    conexao.commit()
    print("Matriz Curricular inserida com sucesso!")

except Exception as ex:
    print("Erro ao inserir dados:", ex)
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conexao' in locals():
        conexao.close()

try:
    conexao = psycopg2.connect(
        user="postgres.muxslmzihfxhaawvvtne",
        password="Foguete50",
        host="aws-0-sa-east-1.pooler.supabase.com",
        port="6543",
        dbname="postgres",
    )
    cursor = conexao.cursor()

    for i in range(len(RA_Hist)):
        Hist_RA = RA_Hist[i]
        Hist_Disc = Disc_Hist[i]
        Hist_Disc_Nome = Nomes_Disc_Hist[i]
        Hist_Sem = Sem_Hist[i]
        Hist_Anos = Anos_Hist[i]
        Hist_Aprov = Aprov_Hist[i]
        Hist_Index = Index_Hist[i]

        

        # Comando SQL para inserir dados
        sql_insert = """
        INSERT INTO "Historico_Aluno" ("RA", "Disc_ID", "Index", "Disc_Nome", "Semestre", "Ano", "Aprovacao")
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql_insert, (Hist_RA, Hist_Disc, Hist_Index, Hist_Disc_Nome, Hist_Sem, Hist_Anos, Hist_Aprov))
    
    conexao.commit()
    print("Histórico de Alunos inserido com sucesso!")

except Exception as ex:
    print("Erro ao inserir dados:", ex)
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conexao' in locals():
        conexao.close()

try:
    conexao = psycopg2.connect(
        user="postgres.muxslmzihfxhaawvvtne",
        password="Foguete50",
        host="aws-0-sa-east-1.pooler.supabase.com",
        port="6543",
        dbname="postgres",
    )
    cursor = conexao.cursor()

    for i in range(len(IDS_Disc)):
        Hist_ID_Prof = Prof_ID_Hist[i]
        Hist_Disc_Prof = IDS_Disc[i]
        Hist_Sem_Prof = Sem_Hist_Prof[i]
        Hist_Anos_Prof = Anos_Hist_Prof[i]
        Hist_Index_Prof = Index_Hist_Prof[i]

        

        # Comando SQL para inserir dados
        sql_insert = """
        INSERT INTO "Historico_Professor" ("Prof_ID", "Disc_ID", "Semestre", "Ano", "Index")
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql_insert, (Hist_ID_Prof, Hist_Disc_Prof, Hist_Sem_Prof, Hist_Anos_Prof, Hist_Index_Prof))
    
    conexao.commit()
    print("Histórico de Professores inserido com sucesso!")

except Exception as ex:
    print("Erro ao inserir dados:", ex)
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conexao' in locals():
        conexao.close()

try:
    conexao = psycopg2.connect(
        user="postgres.muxslmzihfxhaawvvtne",
        password="Foguete50",
        host="aws-0-sa-east-1.pooler.supabase.com",
        port="6543",
        dbname="postgres",
    )
    cursor = conexao.cursor()

    RA_Espec = RA_Reprov[0]
    Nome_Espec = Nome_Reprov[0]
    Curso_Espec = Curso_Reprov[0]
    Sem_Espec = Sem_Reprov[0]

        

    # Comando SQL para inserir dados
    sql_insert = """
    INSERT INTO "Aluno" ("RA", "Nome", "Curso", "Semestre_Atual")
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql_insert, (RA_Espec, Nome_Espec, Curso_Espec, Sem_Espec))
    
    conexao.commit()
    print("Aluno especifico inserido com sucesso!")

except Exception as ex:
    print("Erro ao inserir dados:", ex)
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conexao' in locals():
        conexao.close()

try:
    conexao = psycopg2.connect(
        user="postgres.muxslmzihfxhaawvvtne",
        password="Foguete50",
        host="aws-0-sa-east-1.pooler.supabase.com",
        port="6543",
        dbname="postgres",
    )
    cursor = conexao.cursor()

    for i in range(len(RA_Reprov_Hist)):
        Hist_Reprov_RA = RA_Reprov_Hist[i]
        Hist_Reprov_Disc = Disc_Reprov_Hist[i]
        Hist_Reprov_Disc_Nome = Nome_Disc_Reprov_Hist[i]
        Hist_Reprov_Sem = Sem_Reprov_Hist[i]
        Hist_Reprov_Anos = Anos_Reprov_Hist[i]
        Hist_Reprov_Aprov = Aprov_Reprov_Hist[i]
        Hist_Reprov_Index = Index_Reprov_Hist[i]

        # Comando SQL para inserir dados - DENTRO do loop
        sql_insert = """
        INSERT INTO "Historico_Aluno" ("RA", "Disc_ID", "Index", "Disc_Nome", "Semestre", "Ano", "Aprovacao")
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql_insert, (Hist_Reprov_RA, Hist_Reprov_Disc, Hist_Reprov_Index, Hist_Reprov_Disc_Nome, Hist_Reprov_Sem, 
                                  Hist_Reprov_Anos, Hist_Reprov_Aprov))
    
    conexao.commit()
    print("Historico do aluno especifico inserido com sucesso!")

except Exception as ex:
    print("Erro ao inserir dados:", ex)
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conexao' in locals():
        conexao.close()

try:
    conexao = psycopg2.connect(
        user="postgres.muxslmzihfxhaawvvtne",
        password="Foguete50",
        host="aws-0-sa-east-1.pooler.supabase.com",
        port="6543",
        dbname="postgres",
    )
    cursor = conexao.cursor()

    
    Lec_Prof_ID = ID_Prof_Lec[0]
    Lec_Prof_Nome = Nome_Prof_Lec[0]
    Lec_Dept = Dept_Lec

    # Comando SQL para inserir dados
    sql_insert = """
    INSERT INTO "Professor" ("Prof_ID", "Nome", "Departamento")
    VALUES (%s, %s, %s)
    """
    cursor.execute(sql_insert, (Lec_Prof_ID, Lec_Prof_Nome, Lec_Dept))
    
    conexao.commit()
    print("Professor especifico inserido com sucesso!")

except Exception as ex:
    print("Erro ao inserir dados:", ex)
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conexao' in locals():
        conexao.close()

try:
    conexao = psycopg2.connect(
        user="postgres.muxslmzihfxhaawvvtne",
        password="Foguete50",
        host="aws-0-sa-east-1.pooler.supabase.com",
        port="6543",
        dbname="postgres",
    )
    cursor = conexao.cursor()

    
    for i in range(len(ID_Prof_Lec_Hist)):
        Hist_ID_Prof_Lec = ID_Prof_Lec_Hist[i]
        Hist_ID_Disc_Lec = ID_Disc_Lec_Hist[i]
        Hist_Sem_Lec = Sem_Lec[i]
        Hist_Anos_Lec = Ano_Lec[i]
        Hist_Index_Lec = Index_Lec[i]

        # Comando SQL para inserir dados
        sql_insert = """
        INSERT INTO "Historico_Professor" ("Prof_ID", "Disc_ID", "Semestre", "Ano", "Index")
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql_insert, (Hist_ID_Prof_Lec, Hist_ID_Disc_Lec, Hist_Sem_Lec, Hist_Anos_Lec, Hist_Index_Lec))
    
    conexao.commit()
    print("Historico do professor especifico inserido com sucesso!")

except Exception as ex:
    print("Erro ao inserir dados:", ex)
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conexao' in locals():
        conexao.close()




