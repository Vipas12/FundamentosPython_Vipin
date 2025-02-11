#Fazer um programa para ler quatro números inteiros e positivos, calcular e devolver a suamédia.#
'''num1=int(input("digite o 1º numero: "))
num2=int(input("digite o 2º numero: "))
num3=int(input("digite o 3º numero: "))
num4=int(input("digite o 4º numero: "))
if num1>0 and num2>0 and num3>0 and num4>0:
    print ("a média dos 4 numeros é", (num1+num2+num3+num4)/4)
else:
    print ("pelo menos 1 dos numeros é inteiro.")
'''
'''Fazer um programa para ler quatro números inteiros e positivos, calcular e devolver  a  sua 
média. - usando o ciclo while'''
contador = 0
soma = 0
while contador <4:
    numero = int(input(f"Introduza o {contador+1}º número: "))
    soma = soma + numero     
    contador =contador + 1
    
print(contador)
media = soma / contador
print(f"A média dos números introduzidos é {media}")
    
# x+=1 é o mesmo que x = x + 1
# x-=1 é o mesmo que x = x - 1
# x*=1 é o mesmo que x = x * 1
# x/=1 é o mesmo que x = x / 1
# x%=1 é o mesmo que x = x % 1

#opção 2
contador = 1
soma = 0
while contador <=44:
    numero = int(input(f"Introduza o {contador}º número: "))
    soma = soma + numero     
    contador =contador + 1
print(contador)
media = soma / (contador-1)
print(f"A média dos números introduzidos é {media}")
