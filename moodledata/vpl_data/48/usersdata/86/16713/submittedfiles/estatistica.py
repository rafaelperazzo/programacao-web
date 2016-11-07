# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def sd(lista):
    for i in range(0,len(lista),1):
        cont= cont+(lista[i]-media)**2
        sd=(cont/(len(lista)-1))**0.5
        return sd
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n = input('digite número de elementos:')
a=[]
b=[]
for i in range(0,n,1):
    a.append(input('digite elemento a:'))
for i in range(0,n,1):
    b.append(input('digite elemento b:'))
def media(a):
    soma = 0
    for i in range(0,len(a),1):
        soma = soma + a[i]
    resultado = soma/len(a)
    return resultado
def media(b):
    soma = 0
    for i in range(0,len(b),1):
        soma = soma + b[i]
    resultado = soma/len(b)
    return resultado
media_a=media(a)
media_b=media(b)
cont1=0
for i in range(0,len(a),1):
    cont1= cont1+(a[i]-media_a)**2
sda=(cont1/(len(a)-1))**0.5
cont2=0
for i in range(0,len(b),1):
    cont2= cont2+(b[i]-media_b)**2
sdb=(cont2/(len(b)-1))**0.5
print('%.2f'%media_a)
print('%.2f'%media_b)
print('%.2f'%sda)
print('%.2f'%sdb)