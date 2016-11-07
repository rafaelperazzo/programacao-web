# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def desviopadrao(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+((lista[i]-media(lista))**2
    s=(soma/(n-1))**0.5
    return s
#ETRADA
a=[]
b=[]
n=input('digite a quantidade de elementos:')
#SOLICITANDO OS ELEMENTOS DE A
for i in range (0,n,1):
    a.append(input('digite um elemento:'))
#SOLICITANDO OS ELEMENTOS DE B
for i in range (0,n,1):
    b.append(input('digite um elemento:'))
#CHAMANDO A FUNCAO MEDIA E O DESVIO PADRAO CRIADOS
media_a=media(a)
media_b=media(b)
desviopadrao_a=desviopadrao(a)
desviopadrao_b=desviopadrao(b)

#SAIDA
print ('%.2f' %media_a)
print ('%.2f' %desviopadrao_a)
print ('%.2f' %media_b)
print ('%.2f' %desviopadrao_b)


    