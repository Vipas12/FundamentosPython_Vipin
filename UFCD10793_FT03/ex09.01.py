nome=input("insira o seu nome: ")
idade=input("insira a sua idade: ")
peso=float(input("insira o seu peso: "))
altura=float(input("insira a sua altura em cm: "))
imc = peso / (altura*altura)
print(imc)
if imc < 17:
    print("muito abaixo do peso ideal")
elif imc >= 17 and imc < 18.5:
    print("abaixo do peso ideal")
    
elif imc >= 18.5 and imc < 25:
    print(f"{nome} seu IMC é {imc} você está no peso normal!")
    
elif imc >= 25 and imc < 30:
    
    print(f"{nome} seu IMC é {imc} você está acima do peso!")
    
elif imc >= 30 and imc < 35:
    
    print(f"{nome} seu IMC é {imc} você está em obesidade I!")
elif imc >= 35 and imc < 40:
    
    print(f"{nome} seu IMC é {imc} você está em obesidade II (severa)!")
    
else:
    
    print(f"{nome} seu IMC é {imc} você está em obesidade III (mórbida)!")
    
    
    """nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
IMC = round(peso / (altura * altura), 2)
if IMC < 17:
    
    print(f"{nome} seu IMC é {IMC} você está muito abaixo do peso ideal!")
elif IMC >= 17 and IMC < 18.5:
    print(f"{nome} seu IMC é {IMC} você está abaixo do peso!")
    
elif IMC >= 18.5 and IMC < 25:
    print(f"{nome} seu IMC é {IMC} você está no peso normal!")
    
elif IMC >= 25 and IMC < 30:
    
    print(f"{nome} seu IMC é {IMC} você está acima do peso!")
    
elif IMC >= 30 and IMC < 35:
    
    print(f"{nome} seu IMC é {IMC} você está em obesidade I!")
elif IMC >= 35 and IMC < 40:
    
    print(f"{nome} seu IMC é {IMC} você está em obesidade II (severa)!")
    
else:
    
    print(f"{nome} seu IMC é {IMC} você está em obesidade III (mórbida)!")
    """