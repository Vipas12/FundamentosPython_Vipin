#Escreve uma função em Python que dada uma palavra retorne o número de vogais nessa palavra.

palavra=input('Digite 1 palavra: ')
vogais="aeiouAEIOU"
soma=0
for i in vogais:
    conta=palavra.count(i)
    soma=conta+soma
print(soma)

