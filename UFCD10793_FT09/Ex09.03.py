'''Efetua um programa em python:
a.Instancie o seguinte dicionário:
Computadores_1={
"Marca":"Asus",
"Ecra":"14Pol",
"RAM": [4, 8, 12]
}
b.Acrescente um novo elemento à lista com chave igual a “Disco” e valor [“128G”, “256G”]
c.Permita ao utilizador introduzir um valor específico de RAM e verificar se esta 
está presente na lista.
d.Acrecente 16 como novo valor de RAM.
e.Copie o dicionário para um novo usando Deep Copy().
f.No novo dicionário modifique a marca para “Lenovo” e os valores da RAM para [4,8].
Imprima a nova lista
g.Crie uma nova lista com deep copy e modifique a marca para “HP” e Disco para [“256G”].
Imprima a respetiva lista
h. Cria uma lista cujos elementos são os três dicionários.
i.Imprima as marcas com 128G de Disco
j.Imprima as marcas com 8 e 12 de RAM
'''
'''
computador1 = {
"Marca":"Asus",
"Ecra":"14pol",
"RAM":[4, 8, 12]}

while True:
    user = input("Escolha uma opção:")
    match user:
        case "b":
            computador1.update({"Disco":["128G", "256G"]})
            print(computador1)
        case "c":
            
            computador1.update({"portugues":15})
            computador1.update({"geografia":15})
            print(computador1)
        case "d":
            computador1["RAM"](16)
            del computador1["matematica"]
            print(computador1)
        case "e":
            computador1.popitem()
            print("Removi o último conjunto chave:valor")
            print(computador1)
        case "f":
            computador1.popitem()
            print("Removi o último conjunto chave:valor")
            print(computador1)
        case "g":
            computador1.popitem()
            print("Removi o último conjunto chave:valor")
            print(computador1plinas)
        case "h":
            computador1.popitem()
            print("Removi o último conjunto chave:valor")
            print(computador1)
        case "i":
            computador1.popitem()
            print("Removi o último conjunto chave:valor")
            print(computador1)
        case "j":
            computador1.popitem()
            print("Removi o último conjunto chave:valor")
            print(computador1)
        case _:
            print("Escolha uma opção entre a e d")

del disciplinas["matematica"]
            print(disciplinas)
'''            
            
   
#solução 3            
#Alinea a)

Computadores_1={ "Marca":"Asus",
                 "Ecra":"14Pol",
                 "RAM": [4, 8, 12]}
print(Computadores_1["RAM"][1])
#Alinea b) b.Acrescente um novo elemento à lista com chave igual a “Disco” e valor [“128G”, “256G”]
#Computadores_1["Disco"]=["128G", "256G"]
Computadores_1.update({"Disco":["128G", "256G"]})
print(Computadores_1)



#Alinea c) c.Permita ao utilizador introduzir um valor específico de RAM e verificar se esta está presente na lista
m_ram=int(input("introduza a Capacidade de memoria RAM: "))
if m_ram in Computadores_1["RAM"]:
    print("existe um computador com essa capacidade")
else:
      print("Não existe um computador com essa capacidade")
#Alinea d) d.Acrecente 16 como novo valor de RAM
Computadores_1["RAM"].append(16)
print(Computadores_1)

#Alinea e) e.Copie o dicionário para um novo usando Deep Copy().
computadores_2=Computadores_1.copy()
#Alinea f) No novo dicionário modifique a marca para “Lenovo” e os valores da RAM para [4,8]. Imprima a nova lista
computadores_2["Marca"]="Lenovo"
computadores_2["RAM"]=[4,8]
print(computadores_2)

#Alinea g) Crie uma nova lista com deep copy e modifique a marca para “HP” e Disco para [“256G”]- Imprima a respetiva lista
computadores_3=Computadores_1.copy()
computadores_3["Marca"]="HP"
computadores_3["Disco"]=["256G"]
print(computadores_3)
#Alinea h) Cria uma lista cujos elementos são os três dicionários
lista_pc=[Computadores_1, computadores_2, computadores_3]
#Alinea i) - Imprima marca com 128 G de Disco
marcas=""
for x in lista_pc:
    if "128G" in x["Disco"]:
        marcas = marcas + " "+ x["Marca"]
             
print(marcas)      

#Alinea j)
for x in lista_pc:
    if 8 and 12 in x["RAM"]:
        print("Marcas com 8 e 12G de RAM: ", x["Marca"])
        
for x in computador_all:
if "1TB" in x.get("disco", []):
print(x["marca"])
