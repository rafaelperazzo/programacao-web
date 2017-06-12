# -*- coding: utf-8 -*-
import math

#comece abaixo
def media(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+a[i]
    resultado=soma/len(a)
    return resultado
def dp(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+((a[i]-media(a))**2)
    resultado=(soma/(len(a)-1))**0.5
    return resultado

n=int(input('Quantidade de elementos:'))
a=[]
for i in range(1,n+1,1):
    a.append(int(input('%dº Elemento:'%i)))

print('%.2f'%a[0])
print('%.2f'%a[len(a)-1])
print('%.2f'%media(a))
print('%.2f'%dp(a))