#Criar um programa que leia um ficheiro de texto e exibir o seu conteúdo
with open("exemplo.txt", "r") as ficheiro:
    conteudo=ficheiro.read()
    print(conteudo)


#Modificar o exercício anterior para exibir o conteúdo linha por linha.
with open("exemplo.txt", "r") as ficheiro:
    for linha in ficheiro:
        print(linha.strip())