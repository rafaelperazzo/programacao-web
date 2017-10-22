# -*- coding: utf-8 -*-
d=int(input('digite o valor de d: '))
contador=0
soma=0
while (d>=0):
    if d%10==0:
        soma = soma + (0*2*contador)
    else :
        soma = soma + (1*2*contador)
    d=d/10
    contador=contador+1
print(soma)
    

