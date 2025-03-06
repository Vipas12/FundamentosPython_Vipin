def calcula(ficheiro):
    soma=0
    for i in ficheiro:
        soma=soma+i
  
    media=soma/len(ficheiro)
    
    return soma, media
  
entrada=input("introduz uma lista de numeros separados por espaço: ")

dados=list(map(int, entrada.split())) 
print(dados)

soma, media = calcula (dados)

print("A soma dos elementos da lista é ", soma )
print ("a média é ", media) 
print("o numero de elementos da lista é ", len(dados))
    