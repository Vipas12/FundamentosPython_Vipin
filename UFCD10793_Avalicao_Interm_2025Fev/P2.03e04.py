#Criar um programa que escreva três linhas num ficheiro novo.
with open("novo_ficheiro.txt", "w") as ficheiro:
    ficheiro.write("Linha 1")
    ficheiro.write("Linha 2")
    ficheiro.write("Linha 3")
    
#Modificar o programa anterior para acrescentar mais uma linha ao ficheiro.
with open("novo_ficheiro.txt", "a") as ficheiro:
    ficheiro.write("Linha adicional")