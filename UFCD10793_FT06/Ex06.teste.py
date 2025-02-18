'''try:
    idade = int(input("Digite sua idade: "))
    print("Sua idade é:", idade)
except ValueError:
    print("Erro: Digite um número inteiro válido.")
'''

'''
while True:
    try:
        numero = int(input("Digite um número inteiro positivo: "))
        if numero > 0:
            break  # Sai do loop se o número for válido
        else:
            print("Erro: O número deve ser positivo.")
    except ValueError:
        print("Erro: Digite um número inteiro válido.")

print("Número válido inserido:", numero)
'''


try:
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    print("A divisão é:", a / b)
except ValueError:
    print("Erro: Digite apenas números inteiros.")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")