num=int(input("insira um ano: "))
div_400=num%400
print (div_400)
div_4 = num%4
print (div_4)
div_100 = num%100
if div_400==0:
    print (num, "é numero bisexto")
elif div_4==0 and div_100 !=0:
    print (num, "é numero bisexto")
else:
    print (num, "não é numero bisexto")



''' Elabora um programa para verificar se um ano é bissexto ou não. A condição para ser
um ano bissexto é: o ano deve ser divisível por 400, ou se for divisível por 4 e não for
divisível por 100.'''
'''
ano = int(input("Introduza um ano a fim de averiguar se é Bissexto:"))
if ano % 400 == 0 or (ano % 100 != 0 and ano % 4 == 0):
    print("O ano" , ano, "é Bissexto")
else:
    print("O ano" , ano, "não é Bissexto")
'''