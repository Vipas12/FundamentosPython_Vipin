#Escreve uma função em Python que dada uma palavra retorne o número de vogais nessa palavra.

def contar_vogais(palavra):
    vogais="aeiouAEIOU"
    soma=0
    for i in vogais:
        conta=palavra.count(i)
        soma=conta+soma
    return soma

palavra=input('Digite 1 palavra: ')


soma_vogais=contar_vogais(palavra)
print(f"número de vogais é {soma_vogais}")
