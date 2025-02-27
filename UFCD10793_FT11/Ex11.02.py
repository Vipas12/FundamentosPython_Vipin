def quadrado (lado):
    Area= lado*lado
    Perimetro= 4*lado
    return Area, Perimetro

lado=int(input("Digite o comprimento do lado de um quadrado: "))

Area, Perimetro = quadrado (lado)

print (f"Área:{Area}, Perímetro: {Perimetro}")

