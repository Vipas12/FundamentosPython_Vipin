'''Escreve uma função em Python que, dada uma lista de elementos,
devolva essa mesma lista, mas sem elementos repetidos.'''


import minhasfunc
elemento = input("Escreva uma frase: ")
z = minhasfunc.ex5(elemento)
print(z)

ef ex5(elemento):
    elementos = []
    for p in elemento:
        if p not in elementos:
            elementos.append(p)
    return elementos


