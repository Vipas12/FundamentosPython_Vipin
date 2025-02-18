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


