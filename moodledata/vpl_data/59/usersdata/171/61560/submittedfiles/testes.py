# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
def media(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+a[i]
    media=soma/len(a)
    return(media)
def desvio(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+(a[i]-(media))**2
    desvio=(soma/(n-1))**0.5
    return(desvio)
n=int(input('digite n:'))
a=[]
b=[]
for i in range(0,n,1):
    valor1=float(input('digite o valor para lista a'))
    a.append(valor)
for i in range(0,n,1):
    valor2=float(input('digite o valor para lista b '))
    b.append(valor2)
print('%.2f' %media (a))
print('%.2f' %desvio (a))
print('%.2f' %media (b))
print('%.2f' %desvio (b))