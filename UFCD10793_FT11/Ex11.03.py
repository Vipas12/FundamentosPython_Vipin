def calcula(dados):
    for i in dados:
        soma=soma+i
    
    media=soma/len(dados)
  
entrada=input("introduz uma lista de numeros separados por espaço: ")

dados=list(map(int, entrada.split())) 


calcula (dados)

print("A soma dos elementos da lista é ", soma )
print ("a média é ", media) 
print("o numero de elementos da lista é ", len(dados))
    