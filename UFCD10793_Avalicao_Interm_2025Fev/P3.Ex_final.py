def menu():
    while True:
        print("\n Menu de Gestao de funcionarios")
        print("1. Adicionar funcionario")
        print("2. Listar funcionarios")
        print("3. Atualizar salario")
        print("4. Eliminar funcionario")
        print("5. Sair")
        opcao=input("Escolha uma opção: ")
        if opcao == '1':
            nome= input ("Nome: ")
            cargo= input("Cargo: ")
            salario= float(input("Salario: "))
            cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?,?,?)", (nome, cargo, salario))
        elif opcao == '2':
            cursor.execute("SELECT * FROM funcionarios")
            for funcionario in cursor.fetchall():
                print (funcionario)
        elif opcao == '3':    
            nome= input("Nome do funcionario: ")
            novo_salario= float(input("Introduza novo salario: "))
            cursor.execute("UPDATE funcionarios SET salario= ? WHERE nome= ?", (novo_salario, nome))
        elif opcao=='4':
            nome_eliminar= input("nome do funcionario a eliminar: ")
            cursor.execute("DELETE FROM funcionarios WHERE nome= ?", (nome_eliminar,))
        elif opcao=='5':
            conn.commit()
            conn.close()
            break
        else:
            print("opção inválida! Tente novamente.")

#importar a biblioteca SQL
import sqlite3
#Criar connexão
conn = sqlite3.connect ('empresaEx6_final.db')
cursor=conn.cursor()
#Criar tabela de funcionarios
cursor.execute('''
               CREATE tABLE IF NOT EXISTS funcionarios (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   cargo TEXT NOT NULL,
                   salario REAL NOT NULL
               )
               ''')
#executar def Menu
menu()


        
        
        
    
        