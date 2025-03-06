'''Escreve uma função que, dado o número do mês retorne o mesmo, por extenso'''


def num_mes(mes):
    if mes == '1':
        return 'janeiro'
    if mes == '2':
        return 'fevereiro'
    if mes == '3':
        return 'marco'
    if mes == '4':
        return 'abril'
    if mes == '5':
        return 'maio'
    if mes == '6':
        return 'junho'
    if mes == '7':
        return 'julho'
    if mes == '8':
        return 'agosto'
    if mes == '9':
        return 'setembro'
    if mes == '10':
        return 'outubro'
    if mes == '11':
        return 'novembro'
    if mes == '12':
        return 'dezembro'
    else:
        return 'Erro'

num = input("Digite numero do mês: ")

mes_ano = num_mes (num)

print(mes_ano)
    