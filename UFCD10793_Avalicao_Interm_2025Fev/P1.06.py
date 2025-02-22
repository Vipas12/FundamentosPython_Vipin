'''Elabora uma script em python que peça ao utilizador dois números
e devolva a divisão do primeiro número introduzido pelo seguinte.
Trate erros como divisão por zero e valores inválidos.'''
try:
    numerador=float(input("Digite o numerador: "))
    denominador=float(input("Digite o denominador: "))
    print(f"A divisão dos números é {numerador/denominador:.2f}")
except ValueError:
    print("Erro: Digite um número válido")
except ZeroDivisionError:
    print("Erro: Não é possivel dividir por zero.") 
except Exception as e:
    print("Erro inesperado: ", e)