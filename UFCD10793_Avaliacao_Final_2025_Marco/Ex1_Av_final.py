#Ex1 Leia uma cadeia de caracteres no formato “DD/MM/AAAA” e 
#copie o dia, mês e ano para três variáveis inteiras

data=(input('introduza uma data no formato DD/MM/AAA: '))
dia, mes, ano = [int(i) for i in data.split("/")]
print("dia =", dia, "mes =",mes, "ano =",ano)
