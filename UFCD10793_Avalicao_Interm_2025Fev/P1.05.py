'''Elabora uma script em python que peça ao utilizador um número
e some todos os números de 1 até esse mesmo número.
Deves utilizar o tratamento de erros.'''

try:
    num=int(input("Digite um número: "))
    soma=0
    for i in range(num+1):
        soma=soma+i
    print(soma)
except ValueError:
    print("Erro: Digite um número válido.")
except Exception as e:
    print("Erro inesperado: ", e)
