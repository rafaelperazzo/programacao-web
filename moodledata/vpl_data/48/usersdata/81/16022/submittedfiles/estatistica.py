# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def dpadrao(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+((lista[i] - media(lista))**2)
    dp=((1/(len(lista)-1))*soma)**(1/2) 
    return dp
    
t=[]
d=[]
n=input('Digite a quantidade de elementos:')

for i in range(0,n,1):
    t.append(input('Digite o valor de um elemento de a:'))
for i in range(0,n,1):
    d.append(input('Digite o valor de um elemento de b:'))
    
mediat= media(t)
mediad= media(d)
dpt= dpadrao(t)
dpd= dpadrao(d)

print ('%.2f' %mediat)
print ('%.2f' %dpt)
print ('%.2f' %mediad)
print ('%2f' %dpd)