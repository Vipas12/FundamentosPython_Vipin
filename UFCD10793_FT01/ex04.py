from math import pi
raio = float(input("Escreva o raio da circunferencia: "))
r= raio**3
a=float(4/3)
PII=3.14
print (type(r))
print (type(PII))
print (type(a))
print (type(pi))
volume = r*a*PII
volume1 = r*a*pi
print ("o volume de uma circunferencia de raio", raio, "é de", volume1 )
print (volume1)