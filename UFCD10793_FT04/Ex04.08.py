#Escreve um programa que coloque no ecrã a tabuada do número 5.#
n=int(input("digite o numero da tabuada pretendida: "))
i=0
while i<10:
    i=i+1
    print(n, "x", i, "=", n*i)