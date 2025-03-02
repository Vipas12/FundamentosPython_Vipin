texto = "Teste para ver se funciona o código escrito."

with open("meu_ficheiro.bin", "wb") as ficheiro:
    ficheiro.write(texto.encode("utf-8"))  # Converte e escreve os bytes no ficheiro