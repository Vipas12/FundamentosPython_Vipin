#Resolve a seguinte atividade orientada.
#A ideia é replicar o código e efetuar a respetiva análise.
#1 Criar e gerir uma base de dados utilizando SQLite com Python.
#2 Executar operações básicas: inserção, consulta, atualização e eliminação de dados.
#3 Aplicar comandos SQL dentro de um script Python.

import sqlite3

#Ex_1 Criar conexão com o banco de dados (ou criar se não existir)
conn=sqlite3.connect('empresa.db')
cursor=conn.cursor()

#Criar tabela de funcionarios
cursor.execute('''
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cargo TEXT NOT NULL,
    salario INTEGER)
''')

#Ex_2.1 Inserir funcionários na tabela
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?,?,?)", ('Ana Silva', 'Gestora', 3500))
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?,?,?)", ('Pedro Santos', 'Programador', 3700))
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?,?,?)", ('Mariana Costa', 'Designer', 2000))

#Ex_2.2 Inserir mais 2 funcionários na tabela
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?,?,?)", ('Ana Oliveira', 'Gestora Senior', 4500))
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?,?,?)", ('Alexandre Martins', 'Junior', 1500))

#Ex_3.1 Consultar todos os funcionarios
cursor.execute("SELECT * FROM funcionarios")
funcionarios=cursor.fetchall()

#Ex_3.2 Exibir os resultados
for x in funcionarios:
    print(x)

#Ex_4.1 Atualizar o salario do Pedro Santos
cursor.execute("UPDATE funcionarios SET salario = 3000 WHERE nome = 'Pedro Santos'")

cursor.execute("SELECT * FROM funcionarios WHERE nome=?", ('Pedro Santos',))
funcionario=cursor.fetchone()
if funcionario:
  print(funcionario)
else:
    print("funcionario não encontrado")  

#Ex_4.2 Aumento salarios em 5%
cursor.execute("UPDATE funcionarios SET salario = salario*1.05")
#Exibir os resultados
cursor.execute("SELECT * FROM funcionarios")
funcionarios=cursor.fetchall()
for x in funcionarios:
    print(x)

#Ex_5.1 Remover 1 funcionario da base de dados
cursor.execute("DELETE FROM funcionarios WHERE nome = 'Mariana Costa'")
#Exibir os resultados
cursor.execute("SELECT * FROM funcionarios")
funcionarios=cursor.fetchall()
for x in funcionarios:
    print(x)
    
#Ex_5.2 Remover todos os funcionarios com salario inferior a 3.000 euros
cursor.execute("DELETE FROM funcionarios WHERE salario < 3000")
#Exibir os resultados
cursor.execute("SELECT * FROM funcionarios")
funcionarios=cursor.fetchall()
for x in funcionarios:
    print(x)


# fechar a conexão
conn.commit()
conn.close()



