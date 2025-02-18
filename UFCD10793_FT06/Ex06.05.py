lista = []
while True:
    print("\n1 - Adicionar elemento no início")
    print("2 - Adicionar elemento no fim")
    print("3 - Remover elemento")
    print("4 - Tamanho da lista")
    print("5 - Imprimir elementos da lista")
    print("6 - Esvaziar lista")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

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

