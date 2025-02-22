'''Elabora uma script em python que peça ao utilizador um número
e some todos os números de 1 até esse mesmo número.
Deves utilizar o tratamento de erros.'''

try:
    num=int(input("Digite um número inteiro: "))
    soma=0
    for i in range(num+1):
        soma+= i
    print(f"A soma dos números de 0 a {num} é: {soma}")
except ValueError:
    print("Erro: Digite um número inteiro válido.")
except Exception as e:
    print("Erro inesperado: ", e)
