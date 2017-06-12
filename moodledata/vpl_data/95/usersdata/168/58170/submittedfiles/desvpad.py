# -*- coding: utf-8 -*-
import math

#comece abaixo
def media(a):
    soma=0
    fo i in range (0,len(a),1):
        soma=soma+a[i]
    media=soma/len(a)
    return(media)
def desvio(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+a[i]
    media=soma/len(a)
    soma=0
    for i in range (0,len(a),1):
        dp=(a[j]-media)**2
        somab=soma+dp
    var=soma/len(a)-1)
    desvio=(var)**0.5
    return(desvio)

n=int(input('Digite a quantidade de valores: '))
x=[]
for i in range (0,n,1):
    valor=float(input('Digite os valores da lista: '))
    x.append(valor)
print('%.2f'%x[0]) 
print('%.2f'%x[len(x)-1])  
print('%.2f'%media(x))  
print('%.2f'%desvio(x))  