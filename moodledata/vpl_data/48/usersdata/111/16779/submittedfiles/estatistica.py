# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista

def dp(lista):
    soma=0
    for j in range(0,len(lista),1):
        x=((lista[j]-media(lista))**2)
        soma = soma + x
    p=(soma/(len(lista)-1))**0.5
    return p


n=input('tamanho da lista: ')

a=[]
b = 0
for k in range(0,n,1):
    a.append(input('num:'))
    b=b+a[k]


c=[]
d = 0
for m in range(0,n,1):
    c.append(input('num:'))
    d=d+c[m]
    
    
print('%.2f ' %media(a))
print ('%.2f '  %dp(a))
print ('%.2f ' %media(c))
print ('%.2f ' % dp(c))

    
    

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 