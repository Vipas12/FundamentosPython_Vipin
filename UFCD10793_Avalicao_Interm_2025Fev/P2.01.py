#Criar um programa que leia um ficheiro de texto e exibir o seu conteúdo
with open("exemplo.txt", "r") as ficheiro:
    conteudo=ficheiro.read()
    print(conteudo)