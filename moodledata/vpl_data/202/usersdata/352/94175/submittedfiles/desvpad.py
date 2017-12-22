# -*- coding: utf-8 -*-
import math

#comece abaixo

def desvio_padrao (a):
    somatorio=0
    for i in range (0,len(a),1):
        somatorio=somatorio+((a[i]-media(a))**2)
    desvio=(1/(len(a)-1)*somatorio
    return(desvio)

n=int(input('Quantidade de elementos: '))
a=[ ]

for i in range(0,n,1):
    valor=float(input('Valor: '))
    a.append(valor)
padrao=devvio_padrao(a)
print(padrao)