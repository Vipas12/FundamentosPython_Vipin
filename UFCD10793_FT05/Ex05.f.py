#Escreve um programa, em python, que verifique se uma lista é vazia ou não.
# Caso a lista seja vazia, mostre True, caso contrário False

'''lista=[]
if len(lista)==0:
    print("Lista é vazia#")
else:
    print("a lista não é vazia")
'''

lista=[]
if not len(lista)>0:
    print("Lista vazia")
else:
    print("a lista não é vazia")
