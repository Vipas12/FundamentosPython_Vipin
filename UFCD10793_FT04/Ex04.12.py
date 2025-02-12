#Escreve um programa que calcule e escreva o resultado do fatorial de um
# número inteiro positivo N sabendo que: n!=1*2*3*…*n.#

z=1
x= input("Introduza um número para calcular o seu fatorial: ")
x= int(x)
for i in range(1,x+1):
    z *= i
print(z)