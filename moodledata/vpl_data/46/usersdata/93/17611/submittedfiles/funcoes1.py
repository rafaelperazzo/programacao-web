# -*- coding: utf-8 -*-
from __future__ import division

def crescente(a):
    #escreva o código da função crescente aqui
    for i in range(1,len(a),1):
        if a[i]<=a[i-1]:
            return 'N'
            break
        if i==len(a)-1:
            return 'S'

#escreva as demais funções
def decrescente(a):
    for i in range(1,len(a),1):
        if a[i]>=a[i-1]:
            return 'N'
            break
        if i==len(a)-1:
            return 'S'
def iguais(a):
    for i in range(1,len(a),1):
        if a[i]==a[i-1]:
            return 'S'
            break
        if i==len(a)-1:
            return 'N'
n=input('numero de elementos das listas: ')
a=[]
b=[]
c=[]

for i in range(0,n,1):
    a.append(input('elemento: '))
for i in range(0,n,1):
    b.append(input('elemento: '))
for i in range(0,n,1):
    c.append(input('elemento: '))
print(crescente(a))
print(decrescente(a))
print(iguais(a))
print(crescente(b))
print(decrescente(b))
print(iguais(b))
print(crescente(c))
print(decrescente(c))
print(iguais(c))
#escreva o programa principal
