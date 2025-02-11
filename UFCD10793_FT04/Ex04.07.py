#Elabora um programa para calcula a soma dos N primeiros números naturais (1+2+3+...+N)em que N é um número introduzido pelo utilizador (NOTA: este programa poderia ser feito utilizando a fórmula da progressão aritmética, S = (1+N) * N/2, mas faz de conta que não sabíamos a fórmula).#
n=int(input("digite um numero para soma dos numeros naturais até esse numero: "))
i=0
soma=0
while i<n:
    i=i+1
    soma=soma+i
print(soma)
