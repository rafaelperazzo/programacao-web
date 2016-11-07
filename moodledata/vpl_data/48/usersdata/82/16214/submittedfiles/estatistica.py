# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    media = soma/len(lista)
    return media
a=[]
b=[]
n= input ('Digite a quantidade de elementos:')
for i in range (0,n,1):
    a.append(input('Digite um elemento:'))
for i in range (0,n,1):
    b.append(input('Digite um elemento:'))

media_a = media(a)
media_b = media(b)

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 

def desviopadrao(lista):
    soma=0
    for i in range (0,len(lista),1):
        soma = soma+(lista[i]-media(lista))**2
    s=((1/(len(lista)-1))*soma)**(1/2)
    return s
    
desviopadrao_a=desviopadrao(a)    
desviopadrao_b=desviopadrao(b)

print('%.2f' %media_a)
print('%2.f' %desviopadrao_a)
print('%.2f' %media_b)
print('%2.f' %desviopadrao_b)
