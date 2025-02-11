#Escreve um programa que coloque no ecrã a tabuada do número 5.#
'''n=int(input("digite o numero da tabuada pretendida: "))
i=0
while i<10:
    i=i+1
    print(n, "x", i, "=", n*i)
'''
    
'''Escreve um programa que coloque no ecrã a tabuada do número 5

print("\nTabuada do número 5:")
numero1 = 0
tabuada = 5
multiplicacao = 5
while numero1 <= 10:
    
    multiplicacao = tabuada * numero1 
    print(f"{tabuada} x {numero1} = {multiplicacao}")
    numero1 = numero1 + 1
'''

tabuada=5
for i in range(1,11):
    print(tabuada, "*", i, "=", tabuada * i)
    
#opção2 
numero = int(input("Digite o número para cálcular a tabuada\n---->\t3"))
for x in range (1,11):
    multiplicacao = numero * x
    print (f"{numero}*{x}={multiplicacao}\n")