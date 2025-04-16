# Projeto 1 Banco de Dados

## Autores

Lucas Roberto Boccia dos Santos (22.123.012-1)

Pedro Alexandre Custódio Silva (22.123.049-3)

## Descrição
O projeto 1 de Banco de Dados consiste na implementação de um sistema de banco de dados para uma universidade que seja capaz de armazenar e gerenciar as informações mais comuns do dia a dia de uma unviersidade. Nosso projeto conta com 10 tabelas para armazenar as informações (Aluno, Professor, Departamento, Disciplina, Curso, TCC, TCC Aluno, Matriz Curricular, Histórico Aluno e Histórico Professor).

Tabela Aluno: Armazena o RA (identificador e chave primária) do aluno, o nome do aluno, o curso que o aluno está inserido (que é uma foreign key da tabela Curso) e o semestre atual que o aluno se encontra.

Tabela Professor: Armazena o ID (identificador e chave primária) do professor, o nome do professor e o departamento que o professor faz parte (que é uma foreign key da tabela departamento).

Tabela Departamento: Armazena o ID (identificador e chave primária) do departamento, o nome do departamento e o professor que é chefe do departamento (que é uma foreign key da tabela professor).

Tabela Disciplina: Armazena o ID (identificador e chave primária) da disciplina, o nome da disciplina e o departamento que a disciplina faz parte (que é uma foreign key da tabela departamento).

Tabela Curso: Armazena o ID (identificador e chave primária) do curso, o nome do curso e o professor que é coordenador do curso (que é uma foreign key da tabela professor).

Tabela TCC: Armazena o ID (identificador e chave primária) do TCC, o título do TCC e o professor que é o orientador do TCC (que é uma foreign key da tabela professor).

Tabela TCC Aluno: É formada pela junção das tabelas TCC e Aluno, possuindo o RA do aluno (foreign key da tabela aluno) e o ID do TCC que o aluno está fazendo (que é uma foreign key da tabela TCC).

Tabela Matriz Curricular: É formada pela junção das tabelas Curso e Disciplina, possuindo o ID do curso (que é uma foreign key da tabela curso) e o ID da disciplina (que é uma foreign key da tabela disciplina), além de armazenar o semestre do curso em que cada disciplina é aplicada e possuir uma chave primária "Index", que serve apenas como o identificador das posições da tabela.

Tabela Histórico Aluno: É formada pela junção das tabelas Aluno e Disciplina, possuindo o RA do aluno (que é uma foreign key da tabela aluno), ID e nomes das disciplinas cursadas pelo aluno (que são foreign keys da tabela disciplina) e armazena o semestre do ano em que o aluno cursou a disciplina, o ano em que o aluno cursou a disciplina e se foi ou não aprovado na disciplina. A tabela Histórico Aluno também dispõe de uma coluna "Index" como chave primária, que funciona igualmente à da tabela Matriz Curricular.

Tabela Histórico Professor: É formada pela junção das tabelas Professor e Disciplina, possuindo o ID do professor (que é uma foreign key da tabela Professor), o ID das disciplinas lecionadas por esse professor (que é uma foreign key da tabela Disciplina), e armazena o ano e o semestre do ano em que o professor lecionou tal disciplina. A tabela Histórico Professor também conta com uma chave primária "Index", que funciona da mesma forma que as anteriores.
Os dados genéricos para teste dos relacionamentods da tabela foram gerados pelo arquivo "gerar_info.py" que se encontra disponível no repositório, e foram validados pelo código validacoes.py que também se encontra disponível no repostiório.

## Como Executar
Para executar o projeto, primeiramente deve-se realizar o donwload dos arquivos por meio do Github, selecionar um serviço de banco de dados (como o Supabase, que foi o que utilizamos para os testes) compatível com o PostgreSQL. Após isso, deve-se executar os scripts DDL disponibilizados no repositório para a implementação das tabelas. Para alimentar as tabelas com dados, basta rodar o arquivo "gerar_info.py", adaptando as informações necessárias para conexão com o seu banco de dados (como usuário e senha, que são diferentes para cada usuário). Pode-se validar as informações inseridas utilizando o arquivo "validacoes.py" disponibilizado no repositório. Por fim, testes podem ser feitos utilizando as queries disponibilizadas no repositório, no entanto, pode ser necessário adaptar algumas informações, como os IDs utilizados, se forem geradas novas informações para o banco de dados.

## Modelo Relacional

![MR](https://github.com/user-attachments/assets/81cc88a3-b1cf-4986-947c-a046f6853987)

## Modelo Entidade Relacionamento

![MER](https://github.com/user-attachments/assets/6a63cc8d-5535-4414-a8bd-d2f2cdee7cee)


