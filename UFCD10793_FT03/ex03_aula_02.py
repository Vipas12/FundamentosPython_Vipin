num1=float(input("insira o 1º numero inteiro: "))
num2=float(input("insira o 2º numero inteiro: "))
operação=input("introduza a operaçao: +, -, /, *")
match operação:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        if num2 == 0:
            print ("não pode dividir um numero por 0")
        else
        print(num1 / num2)
    case _:
        print("operação inválida")
        
        
        
        
    