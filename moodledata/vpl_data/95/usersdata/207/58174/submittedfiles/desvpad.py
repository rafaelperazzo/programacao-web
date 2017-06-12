# -*- coding: utf-8 -*-
import math

def media(a):
    soma=0
    for v in range (0,len(a),1):
        soma=soma+a[v]
    media=soma/len(a)
    return(media)
    
def desvio(a):
    soma=0
    for v in range (0,len(a),1):
        soma=soma+a[v]
    media=soma/len(a)
    sdq=0
    for l in range (0,len(a),1):
        dq=(a[l]-media)**2
        sdq=sdq+dq
    var=sdq/(len(a)-1)
    desvio=var**0.5
    return(desvio)

n=int(input('escreva a quantidade dos valores da lista:'))
x=[]
for i in range (1, n+1, 1):
    valor=float(input('escreva os valores da lista:'))
    x.append(valor)
print('%.2f'%x[0])
print('%.2f'%x[len(x)-1])
print('%.2f'%media(x))
print('%.2f'%desvio(x))
    


