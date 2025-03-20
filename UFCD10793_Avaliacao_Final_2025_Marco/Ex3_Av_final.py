#Escreve uma função em Python que dada uma lista de números imprime 
# a soma dos valores dessa lista, o número de elementos da lista e a media desses valores.
# Implementa tratamento de exceções no teu código (try…except…else..finally).

lista= [int(input("insira uma lista de numeros: "))]
#lista1 = [1,2,3,4,5,6,7,8,9,10,11]
soma_lista=sum(lista)
tamanho_lista=len(lista)
print("a soma da lista é ",soma_lista)
print("o tamanho da lista é ",tamanho_lista)
print("a média dos valores da lista é ", float(soma_lista/tamanho_lista))

