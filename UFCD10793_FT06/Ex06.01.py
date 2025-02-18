'''
Considere a seguinte lista
cores=["amarelo", "azul", "branco", "preto", "verde"]
Cria um programa, em python, que:
a. Faz o print de toda a lista
b. Faz o print do indíce 2 da lista
c. Altera o indíce 0 da lista para "vermelho"
d. Faz o print de toda a lista
e. Acrescenta no final da lista a cor "amarelo"
f. Faz o print de toda a lista
g. Acrescenta no indíce 2 a cor "roxo"
h. Faz o print de toda a lista
i. Apaga o último elemento da lista
j. Faz o print de toda a lista
k. Faz o print do tamanho da lista (len)
'''

'''
cores = ["amarelo","azul","branco","preto","verde"]
print(cores)
print(cores[1])
cores[0]="vermelho"
print(cores)
cores.append("amarelo")
print(cores)
cores.insert(2,"roxo")
print(cores)
cores.pop()
print(cores)
print(len(cores))
'''


cores = ["amarelo","azul","branco","preto","verde"]
print(cores)
cores = ["amarelo","azul","branco","preto","verde"]
print(cores[2])
cores = ["amarelo","azul","branco","preto","verde"]
cores[0]="vermelho"
print(cores)
cores = ['vermelho', 'azul', 'branco', 'preto', 'verde']
cores.append('amarelo')
print(cores)
cores=['vermelho', 'azul', 'branco', 'preto', 'verde', 'amarelo']
cores.insert(2,"roxo")
print(cores)
cores=['vermelho', 'azul', 'roxo', 'branco', 'preto', 'verde', 'amarelo']
cores.pop()
print(cores)
cores=['vermelho', 'azul', 'roxo', 'branco', 'preto', 'verde']
tamanho=len(cores)
print(tamanho)

'''

cores=["amarelo", "azul", "branco", "preto", "verde"]

while True:
    print("a - Imprimir elementos da lista")
    print("b - Imprimir elemento posicao 3)
    
    print("\n 1 - Adicionar elemento no início")
    print("2 - Adicionar elemento no fim")
    print("3 - Remover elemento")
    print("4 - Tamanho da lista")
    print("5 - Imprimir elementos da lista")
    print("6 - Esvaziar lista")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")
    
    elif opcao == "a":
        print("Elementos da lista:", cores)
        
    if opcao == "1":
        elemento = input("Digite o elemento a adicionar no início: ")
        lista.insert(0, elemento)

    elif opcao == "2":
        elemento = input("Digite o elemento a adicionar no fim: ")
        lista.append(elemento)

    elif opcao == "3":
        if lista:
            elemento = input("Digite o elemento a remover: ")
            if elemento in lista:
                lista.remove(elemento)
            else:
                print("Elemento não encontrado.")
        else:
            print("A lista está vazia.")

    elif opcao == "4":
        print("Tamanho da lista:", len(lista))

    elif opcao == "5":
        print("Elementos da lista:", lista)

    elif opcao == "6":
        lista.clear()
        print("A lista foi esvaziada.")

    elif opcao == "7":
        print("A sair do programa...")
        break

    else:
        print("Opção inválida, tente novamente.")
'''


