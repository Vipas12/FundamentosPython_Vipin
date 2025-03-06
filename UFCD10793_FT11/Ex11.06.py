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
   
   
   
   
   
   
import main_funcoes as mf # Importa o módulo main_funcoes.py
input_mes = int(input("Digite o número do mês: ")) # Solicita o número do mês ao usuário
res = mf.mes_extenso(input_mes) # Chama a função mes_extenso do módulo main_funcoes
print(f"O mês {input_mes} é {mf.mes_extenso(input_mes)}") # Imprime o mês por extenso 

# Escreve uma função que, dado o número do mês retorne o mesmo, por extenso.
def mes_extenso(mes):
    # Dicionário com os meses do ano
    meses = {
        1: 'Janeiro',
        2: 'Fevereiro',
        3: 'Março',
        4: 'Abril',
        5: 'Maio',
        6: 'Junho',
        7: 'Julho',
        8: 'Agosto',
        9: 'Setembro',
        10: 'Outubro',
        11: 'Novembro',
        12: 'Dezembro'
    }
    
    # Retorna o mês por extenso
    return meses.get(mes, 'Mês inválido')