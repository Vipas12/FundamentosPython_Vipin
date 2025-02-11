#Escreve um programa que calcule a soma e o produto dos N primeiros números naturais#
"""i=1
while i<=5:
    print(f"{i}\t{i**2}")
    i=i+1
"""
y=0
z=1
x= input("Introduza um número para calcular a soma: ")
x= int(x)
for i in range(1,x+1):
    y += i
    z *= i
    
print(y)
print(z)