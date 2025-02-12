#Escreva um programa que peça ao utilizador números entre 0-10.
# Se o utilizador inserir um número fora desse intervalo o programa
# deverá finalizar com uma mensagem personalizada
'''n=int(input("insira um numero entre 0 e 10: "))
if n>10 or n<0:
    print("numero inserido não está dentro do intervalo 0 e 10")
'''
n=int(input("insira um numero entre 0 e 10: "))
while n>10 or n<0:
    print("numero inserido não está dentro do intervalo 0 e 10")
    break
