# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def desvio(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma + lista[i]
    resultado= soma +(lista[i]-media)**2
    s=((1/(n-1))*soma)**0.5


n=input('Digite o s valores da lista:')

a=[]
b=[]

for i in range(0,n,1):
    a.append(input('Acrescente valores a lista:'))
    
for i in range(0,n,1):
    b.append(input('Acrescente valores a lista:'))
    
media_a=media(a)
media_b=media(b)

print('%.2f'media_a)
print('%.2f'desvio_a)
print('%.2f'media_b)
print('%.2f'desvio_b)
    
    
    