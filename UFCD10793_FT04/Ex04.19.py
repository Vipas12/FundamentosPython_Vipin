#Escreve um programa que solicite ao utilizador um número e escreva em simultâneo
# a sequência crescente e decrescente entre 1 e esse número.
a=int(input("insira um numero superior a 1: "))
if a<1:
    print("numero é inferior a 1")
else:   
    for i in range(1,a+1):
        print(i, a+1-i)
        i=i+1