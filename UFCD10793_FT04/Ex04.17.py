#Escreva um programa que peça ao utilizador 20 números reais e no final
# mostre a soma e a médiados números introduzidos.
soma=0
media=0
for i in range(20):
    a=float(input("Digite um numero de uma sequencia de 20 numeros: "))
    soma=soma+a
media=soma/20
print(soma, media)