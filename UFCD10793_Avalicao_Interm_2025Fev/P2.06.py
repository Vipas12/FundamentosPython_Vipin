#Cria ou faz download de um ficheiro CSV.
# De seguida cria um programa que leia o ficheiro CSV e mostre cada linha do mesmo.
import csv

#opçao1
dados=[["Nome", "Idade"], ["João", 25], ["Ana", 30]]
with open("dados.csv", "w", newline="", encoding="utf-8") as ficheiro:
    escritor=csv.writer(ficheiro)
    escritor.writerows(dados)

#opção2
with open("dados.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo) # Escrever cabeçalho
    escritor.writerow(["Nome", "Idade", "Cidade"])
    # Escrever dados
    escritor.writerow(["Alice", 25, "Lisboa"])
    escritor.writerow(["Bruno", 30, "Porto"])
    escritor.writerow(["Carlos", 22, "Faro"])

#mostrar ficheiro linha a linha
with open("dados.csv", newline='', encoding="utf-8") as ficheiro:
    leitor=csv.reader(ficheiro)
    for linha in leitor:
        print(linha)
