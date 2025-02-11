#Implemente um programa que, dada uma letra (S, C ou V), indique o estado civil deuma pessoa.#
estado_civil = str(input("Digite a letra do seu estado civil: C, S, V: "))
match estado_civil:
    case "c":
        print ("O seu estado civil é casado")
    case "s":
        print ("O seu estado civil é solteiro")
    case "v":
        print ("O seu estado civil é viúvo")
    case _:
        print ("Estado civil incorretamente digitado")
        
        
