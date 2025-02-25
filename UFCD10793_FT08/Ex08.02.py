texto=input("Introduza um texto: ")
pontuacao=[".", "?", "!", ";",":", "," ]

for p in pontuacao:
    texto=texto.replace(p,"")
numPalavras=len(texto.split())
print("Numero palavras: ", numPalavras)
    
