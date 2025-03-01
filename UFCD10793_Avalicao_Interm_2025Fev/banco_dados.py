#Resolve a seguinte atividade orientada.
#A ideia é replicar o código e efetuar a respetiva análise.
#1 Criar e gerir uma base de dados utilizando SQLite com Python.
#2 Executar operações básicas: inserção, consulta, atualização e eliminação de dados.
#3 Aplicar comandos SQL dentro de um script Python.

import sqlite3

#Criar conexão com o banco de dados (ou criar se não existir)
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

#Inserir funcionários na tabela
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?,?,?)", ('Ana Silva', 'Gestora', 3500))
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?,?,?)", ('Pedro Santos', 'Programador', 3700))
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?,?,?)", ('Mariana Costa', 'Designer', 2000))

#Inserir mais 2 funcionários na tabela
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?,?,?)", ('Ana Oliveira', 'Gestora Senior', 4500))
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?,?,?)", ('Alexandre Martins', 'Junior', 1500))


#consultar todos os funcionarios
cursor.execute("SELECT * FROM funcionarios")
funcionarios=cursor.fetchall()

#Exibir os resultados
for i in funcionarios:
    print(i)


# fechar a conexão
conn.commit()
conn.close()



