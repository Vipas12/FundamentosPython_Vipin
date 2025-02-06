num1=float(input("insira o 1º numero inteiro: "))
num2=float(input("insira o 2º numero inteiro: "))
operacao=input("introduza a operaçao: +, -, /, *")
match operacao:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        if num2 == 0:
            print ("não pode dividir um numero por 0")
        else:
            print(num1 / num2)
    case _:
        print("operação inválida")

'''
num1=int(input("Digita o primeiro número:\n---->\t"))
num2=int(input("Digita o segundo número:\n---->\t"))
operacao = input("Seleciona a operação a realizar (+, -, *, /):\n---->\t")
match operacao:
    case "+":
        resultado = num1 + num2
    case "-":
        resultado = num1 - num2
    case "*":
        resultado = num1 * num2
    case "/":
        if num2 == 0:
            resultado = "Divisão por zero não é permitida"
        else:
            resultado = num1 / num2
    case _:
        resultado = "Operação inválida"
print("Resultado:", resultado)
com duas // apresenta a divisão inteira
'''
        
        
        
    