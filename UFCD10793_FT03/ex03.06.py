num1=float(input("insira o 1º numero inteiro: "))
num2=float(input("insira o 2º numero inteiro: "))
num3=float(input("insira o 3º numero inteiro: "))

if num1>=num2 and num1>=num3:
    print ("o 1º numero", num1, "é maior dos numeros 2 e 3")
elif num2>=num1 and num2>=num3:
    print ("o 2º numero", num2, " é maior dos numeros 1 e 3")
elif num3>=num1 and num3>=num2:
    print ("o 3º numero", num3, " é maior dos numeros 1 e 2")
else:
    print ("impossível. Rever o código")