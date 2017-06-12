# -*- coding: utf-8 -*-
import math

def media(a):
    soma=0
    for j in range (0, len(a), 1):
        soma=soma+a[j]
    media=soma/len(a)
    return(media)
    
def desvio(a):
    soma=0
    for j in range (0, len(a), 1):
        soma=soma+a[j]
    media=soma/len(a)
    sdq=0
    for k in range (0, len(a), 1):
        dq=(a[k]-media)**2
        sdq=sdq+dq
    var=sdq/(len(a)-1)
    desvio=var**0.5
    return(desvio)
    
a=int(input('Digite a quatidade de valores da lista:'))
b=[]
for i in range (1,a+1, 1):
    valor=float(input('Digite os valores da lista:'))
    b.append(valor)
print('%.2f' %b[0])
print('%.2f' %b[len(b)-1])    
print('%.2f' %media(b))    
print('%.2f' %desvio(b))   


