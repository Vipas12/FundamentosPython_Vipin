'''Escreva um programa que,dada uma sequência de números inteiros
(todosfornecidosnamesmalinha,separadosporespaços),imprimaamédiadessesnúmeros.'''
string ="1 2 3 4 5 6 7 8 9 10"
#string=input("introduza numeros inteiros separados por espaço: ")
lista=string.split()
print(lista)
print(len(lista))
soma=0
for n in lista:
    soma=soma+int(n)
print(soma)
media=soma/len(lista)
print (soma/len(lista))
print("A média dos números é", format(soma/len(lista), ".2f"))
    
