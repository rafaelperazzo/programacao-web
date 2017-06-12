# -*- coding: utf-8 -*-
import math

#comece abaixo
def media(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+a[i]
    media=soma/len(a)
    return (media)
def dp(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+a[i]
    media=soma/(len(a)
    somab=0
    for j in range(0,len(a0,1):
        dp=(a[j]-media)**2
        somab=somab+dp
    var=somab/(len(a)-1)
    desvio=(var)**0.5
    return(desvio)

n=int(input('quantidade de elementos:'))
a=[]
for i in range(0,n,1):
    valor=float(input('elemntos:')):
        a.append(valor)
    
print('%.2f'%a[0])
print('%.2f'%a[len(a)-1])
print('%.2f'%media(a))
print('%.2f'%dp(a))