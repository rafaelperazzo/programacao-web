# -*- coding: utf-8 -*-
d=int(input('digite o valor de d: '))
i=0
soma=0
while (d>0):
    ultimo=d%10
    normal=ultimo*(2**i)
    soma=soma+normal
    i=i+1
    d=d//10
print(soma)
    

