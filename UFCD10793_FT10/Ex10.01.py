'''Reproduz o seguinte programa'''
txt="  uFcd proGRAMação eM pyTHON"
#imprimir texto
print(txt)
#imprimir texto sem espaçamento
txt=txt.strip()
print(txt)
#imprimir texto até a palavra 13ª posição
print(txt[:13])
#imprimir ultimos 3 carateres
print(txt[-5:])
txt=txt.upper()
print(txt)

nome="Sandra Oliveira"
print("O {} gosta muito da {}".format(nome, txt))
print(f"O {nome} gosta muito da {txt}")

