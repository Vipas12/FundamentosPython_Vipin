'''import random
numero_aleatorio = random.randint(1, 100)
print(numero_aleatorio)
'''
'''
from random import randint
num1 = randint(1, 100)
num = num1
print(num)
 #O que se está a passar? Se eu tirar esta linha, o programa está constantemente a dizer que o número q insiro é maior do que o num. Mesmo que escreva 100
while True:
    try:
        utilizador = int(input("Advinha o número secreto:\n"))
        if utilizador == num:
            print("Você acertou, parabéns!")
            break
        elif utilizador > num:
            print(f"{utilizador} é maior do que o número secreto! Tenta outra vez")
        elif utilizador < num:
            print(f"{utilizador} é menor do que o número secreto! Tenta outra vez")
    except ValueError:
        print("Indica um número inteiro, entre 1 a 100, por favor")
'''


from random import randint
num = randint(1, 100)
#O que se está a passar? Se eu tirar esta linha, o programa está constantemente a dizer que o número q insiro é maior do que o num. Mesmo que escreva 100
while True:
    try:
        utilizador = int(input("Advinha o número secreto:\n"))
        if utilizador == num:
            print("Você acertou, parabéns!")
            break
        elif utilizador >= num:
            print(f"{utilizador} é maior do que o número secreto! Tenta outra vez")
        elif utilizador <= num:
            print(f"{utilizador} é menor do que o número secreto! Tenta outra vez")
    except ValueError:
        print("Indica um número inteiro, entre 1 a 100, por favor")