'''Efetua um programa em python onde:
a.Cries um dicionário e efetues o respetivo print.
b.Acrescentes dois novos elementos ao dicionário.
c.Removes um dos elementos da lista;
d.Efetues uma operação, à escolha, sobre os dados no dicionário
'''

'''dados=input("introduza um dicionario: ")
print(dados)
dados.update({"x": 1, "z": 6})
'''


disciplinas = {"matematica":15, "ingles":16, "historia":16}
while True:
    user = input("Escolha uma opção:")
    match user:
        case "a":
            print(disciplinas)
        case "b":
            disciplinas.update({"portugues":15})
            disciplinas.update({"geografia":15})
            print(disciplinas)
        case "c":
            del disciplinas["matematica"]
            print(disciplinas)
        case "d":
            disciplinas.popitem()
            print("Removi o último conjunto chave:valor")
            print(disciplinas)
        case _:
            print("Escolha uma opção entre a e d")
