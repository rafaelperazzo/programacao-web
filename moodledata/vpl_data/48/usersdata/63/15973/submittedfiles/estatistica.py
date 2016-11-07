# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def dp(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    resultado=soma+(lista[i]-media)**2
    s=((1/(n-1))*soma)**0,5
    return resultado

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 

n=input('Numero de elementos:')
a=[]
b=[]

for i in range (0,n,1):
    a.append(input('Valores da lista:'))
    
for i in range(0,n,1):
    b.append(input('Valores da lista:'))

media_a=media(a)
media_b=media(b)

print ('%.2f'%media_a)
print ('%.2f'%dp_a)
print ('%.2f'%media_b)
print ('%.2f'%dp_b)


    