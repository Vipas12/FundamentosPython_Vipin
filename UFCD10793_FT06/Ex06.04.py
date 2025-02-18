'''
sinstance(x,int) and not isinstance(x,bool)
isinstance(x,float)
isinstance(x,str)
isinstance(x,bool)
type(x)==int
type(x)==bool
type(x)==str
type(x)==float

a. Imprima a quantidade de inteiros, floats, strings e boleanos na lista;
b. Efetua a média de todos os valores inteiros na lista.
c. Crie e retorne uma nova lista só com os valores inteiros

'''
c_int=0
c_float=0
c_str=0
c_bool=0

nums=[10, 2.5, 7, 11, 7.9, "Python", True,6, 5.8 , "Listas"]

for x in nums:
    if type(x)==int:
        c_int=c_int+1
        continue
    if type(x)==float:
        c_float=c_float+1
        continue
    if type(x)==str:
        c_str=c_str+1
        continue
    if type(x)==bool:
        c_bool=c_bool+1
    #tb dá para fazer com elif

inteiros = sum(1 for x in nums if isinstance(x, int) and not isinstance(x, bool))
floats = sum(1 for x in nums if isinstance(x, float))
strings = sum(1 for x in nums if isinstance(x, str))
booleanos = sum(1 for x in nums if isinstance(x, bool))