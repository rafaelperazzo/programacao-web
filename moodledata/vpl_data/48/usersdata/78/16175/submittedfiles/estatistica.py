# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
    
def desvioP(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+(lista[i]-media(lista)**2)
    resultado=((soma/len(lista)-1)**0.5)
    return resultado    

a=[]
b=[]
n=input('digite o valor de n:')

for i in range (0,n,1):
    a.append(input('digite os elementos da lista1:'))

for i in range (0,n,1):
    b.append(input('digite os elementos da lista2:'))
    
    
media_a=media(a)
media_b=media(b)
s_a=desvioP(a)
s_b=desvioP(b)

print('%.2f' %media_a)
print('%.2f' %s_a)
print('%.2f' %media_b)
print('%.2f' %s_b)
    
    
    
    
    
    
    
    
    
    