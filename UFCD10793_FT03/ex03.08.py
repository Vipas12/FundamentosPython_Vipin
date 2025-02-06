num1=float(input("insira o 1º numero inteiro: "))
num2=float(input("insira o 2º numero inteiro: "))
num3=float(input("insira o 3º numero inteiro: "))

if num1==num2 and num1==num3:
    print ("triangulo equilatero, todos os lado possuem o mesmo comprimento")
elif num2!=num1 and num2!=num3:
    print ("triangulo escaleno: todos os lados possuem diferentes comprimentos")
elif num1==num2 and num2!=num3:
    print ("triangulo isosceles")
elif num2==num3 and num2!=num1:
    print ("triangulo isosceles")
elif num1==num3 and num1!=num2:
    print ("triangulo isosceles")
else:
    print ("impossível. Rever o código")
    
    
'''Ex 08
lado_a = float(input("Digite o primeiro lado\n "))
lado_b = float(input("Digite o segundo lado\n "))
lado_c = float(input("Digite o terceiro lado\n "))
if lado_a == lado_b == lado_c:
    print("Triângulo equilátero")
elif lado_a != lado_b != lado_c:
    print("Triângulo escaleno")
else:
    print("Triângulo isósceles")'''
    
    