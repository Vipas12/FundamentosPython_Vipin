# Elabora um programa que pede ao utilizador para inserir dois números inteiros.
# O programa deve escrever todos os números inteiros entre os dois limites por ordem crescente.
# Utiliza o ciclo for.
a=int(input("digite o limite inferior: "))
b=int(input("digite o limite superior: "))
if a<b:
    for i in range(a,b+1,1):
        print(i)
else:
    print("erro, limite inferior superior ao limite superior")
