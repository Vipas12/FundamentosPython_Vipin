#Cria ou faz download de um ficheiro CSV.
# De seguida cria um programa que leia o ficheiro CSV e mostre cada linha do mesmo.
import csv

dados=[["Nome", "Idade"], ["João", 25], ["Ana", 30]]
with open("dados.csv", "w", newline="", encoding="utf-8") as ficheiro:
    escritor=csv.writer(ficheiro)
    escritor.writerows(dados)

with open("dados.csv", mode="w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo) # Escrevendo cabeçalho
    escritor.writerow(["Nome", "Idade", "Cidade"])
    # Escrevendo dados
    escritor.writerow(["Alice", 25, "Lisboa"])
    escritor.writerow(["Bruno", 30, "Porto"])
    escritor.writerow(["Carlos", 22, "Faro"])



with open("dados.csv", newline='', encoding="utf-8") as ficheiro:
    leitor=csv.reader(ficheiro)
    for linha in leitor:
        print(linha)
