# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
def dp(lista):
    sama=0
    for i in range(0,len(lista),1):
        sama=sama+((lista[i]-media(lista))**2)
        dp=((sama/(len(lista)-1))**0.5)
    return dp

n=input('digite a quantidade de termos das listas:')
a=[]
b=[]

for i in range(0,n,1):
    a.append(input('digite o valor:'))
for i in range(0,n,1):
    b.append(input('digite os elementos de b:'))
media_a=media(a)
media_b=media(b)
dp_a=dp(a)
dp_b=dp(b)

print ('%.2f'%media_a)
print('%.2f'%dp_a)
print ('%.2f'%media_b)
print('%.2f'%dp_b)
