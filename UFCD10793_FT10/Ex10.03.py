'''Considere a seguinte variável que armazena uma string
com um conjunto de datas separadas pelo caracter “,”.'''

'''Crie programa para:
A - Armazene as diferentes datas numa string;
B - Imprima as datas correspondentes ao ano de 2022;
C - Crie uma noca lista (dias) e na mesma armazena o dia de cada uma das datas.
Ordene a lista de forma crescente e imprima a mesma.'''

datas="12ago2021,02set2020,20jan2022,11out2019,09mar2020,10dez2022"
lista=datas.split(",")
print(lista)
for i in lista:
    if "2022" in i:
        print(i)

dias=[]
for n in lista:
    dias.append(n[:2])
dias.sort()
print(dias)

