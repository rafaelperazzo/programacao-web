# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
cont=0
for i in range(0,len(lista),1):
    cont= cont+(lista[i]-media)**2
sd=(cont/(len(lista)-1))**0.5
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n = input('digite número de elementos:')
a=[]
b=[]
for i in range(0,n,1):
    a.append(input('digite elemento:'))
for i in range(0,n,1):
    b.append(input('digite elemento:'))
def media(a):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
def media(b):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
media_a=media(a)
media_b=media(b)
for i in range(0,len(a),1):
    cont= cont+(a[i]-media_a)**2
sda=(cont/(len(a)-1))**0.5
for i in range(0,len(b),1):
    cont= cont+(b[i]-media_b)**2
sdb=(cont/(len(b)-1))**0.5
print('%.2f'%media_a)
print('%.2f'%media_b)
print('%.2f'%sda)
print('%.2f'%sdb)