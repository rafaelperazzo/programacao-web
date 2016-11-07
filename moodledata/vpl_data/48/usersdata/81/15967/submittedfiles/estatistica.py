# -*- coding: utf-8 -*-
from __future__ import division

def media(t,d):
    soma = 0
    for i in range(0,len(t,d),1):
        soma = soma + t,d[i]
    resultado = soma/len(t,d)
    return resultado

def dpadrao(t,d):
    soma=0
    for i in range(0,len(t,d),1):
        soma=soma+(((lista[i] - media(t,d))**2)
    dp=((1/(len(t,d)-1))*soma)**(1/2) 
    return dp
    
t=[]
d=[]
n=input('Digite a quantidade de elementos:')

for i in range(0,n,1):
    t.append(input('Digite o valor de um elemento de a:')
for i in range(0,n,1):
    d.append(input('Digite o valor de um elemento de b:')
    
mediat= media(t)
mediad= media(d)
dpt= dpadrao(t)
dpd= dpadrao(d)

print ('%.2f' %mediat)
print ('%.2f' %dpt)
print ('%.2f' %mediad)
print ('%2f' %dpd)