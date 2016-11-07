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
    resultadoo= soma +(lista[i]-resultado)**2
    s=((1/(n-1))*soma)**0.5
    return resultadoo
    

n=input('Digite o s valores da lista:')

a=[]
b=[]

for i in range(0,n,1):
    a.append(input('Acrescente valores a lista:'))
    
for i in range(0,n,1):
    b.append(input('Acrescente valores a lista:'))
    
mediaA=media(a)
mediaB=media(b)
desvioA=desvio(a)
desvioB=desvio(b)

print('%.2f' %mediaA)
print('%.2f'%desvioA)
print('%.2f'%mediaB)
print('%.2f'%desvioB)
    
    
    