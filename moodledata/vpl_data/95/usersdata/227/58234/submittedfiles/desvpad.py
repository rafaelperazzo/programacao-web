# -*- coding: utf-8 -*-
import math

#comece abaixo
def media(a):
    for j in range(0,len(a),1):
        soma=soma+a[j]
        media=soma/len(a)
        return(media)
def desvio(a):
    soma=
    for j in range(0,len(a),1):
        soma=soma+a[j]
    media=soma/len(a)
    sdq=0
    for k in range (0, lend(a),1):
        dq=(a[k]-media)**2
        sdq=sdq+dq
    var=sdq/(len(a)-1)
    descio=var**0.5
    return(desvio)
n=int(inpur('Digite a quantidade de valores da lista:'))
x=[]
for i in range (1.n+1.1):
    valor=float(input('Digite os valores da lista:'))
    x.append(valor)
print('%.2f'%x{0])
print('%.2f'%x{len(x)-1])
print('%.2f'%media(x))
print('%.2f'%desvio(x))