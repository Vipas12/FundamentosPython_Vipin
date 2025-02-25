'''Escreve um programa em Python que
A - Imprima o texto anterior todo em maiúsculas;
B - Peça uma palavra ao utilizador e verifique se a mesma está ou não no texto,
devolvendo o resultado ao utilizador.
C - Imprima o número de vezes que a letra "O" ocorre no texto
D - Substitua todas as ocorrências da letra "P" no texto por "_"
'''

txt="""Python é uma linguagem de programação 3 de 3 de alto nível,
interpretada de script, imperativa, orientada a objetos,
funcional, de tipagem dinâmica e forte."""

txtM=txt.upper()
print(txtM)

palavra=input("introduza palavra para procurar:")
if palavra in txt:
        print(True)
else:
    print(False)


#c. Imprima o número de vezes que a letra ‘O’ ocorre no texto
print(txt.count("o"))
#b. Peça uma palavra ao utilizador e verifique se a mesma está ou não no texto, devolvendo o resultado ao utilizador.
print( input("qual a palavra de pesquisa -") in txt)
#d. Substitua todaa as ocorrências da letra ‘P’ no texto por ‘_’
y=txt.replace("p","_")
print(y)

