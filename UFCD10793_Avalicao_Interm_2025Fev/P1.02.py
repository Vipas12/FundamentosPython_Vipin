'''Peça dois números ao utilizador e trate a divisão por zero.'''
try:
    num1=int(input("digite o numerador: "))
    num2=int(input("digite o denominador: "))
    print("Resultado da divisão:", num1/num2)
except ZeroDivisionError:
    print("Erro: não 0possivel dividir por zero.")
except ValueError:
    print("Erro: Apenas números inteiro são permitidos")


