'''Escreva um programa que pede ao utilizador um número inteiro e trata erros de entrada.
'''
try:
    num=int(input("Digite número inteiro: "))
    print("Número inserido:", num)
except ValueError:
    print("Erro: o valor deve ser um número inteiro")




