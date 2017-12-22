# -*- coding: utf-8 -*-
nm=int(input('digite o numero de elementos da primeira lista:'))
mn=int(input('digite o numero de elementos da segunda lista:'))
e=[]
va=[]

for i in range(0,nm,1):
    valor_e=float(input('digite um elemento da primeira lista:'))
    e.append (valor_e)
for i in range(0,mn,1):
    valor_va=float(input('digite um elemento da segunda lista:'))
    va.append (valor_va)

def intersecao(e,va):
    return list (set(e) & set(va))
intersecao=intersecao(e,va)
print(len(intersecao))
