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
