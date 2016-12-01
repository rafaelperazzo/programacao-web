# -*- coding: utf-8 -*-
from __future__ import division

def somavida(n,e,s):
    i=e
    soma=0
    while i<=s:
        soma=soma+n[i]
        i=i+1
    return soma

n=input('qnt de sala:')
e=input('porta de entrada:')
s=input('porta de saida:')
a=[]
for i in range(0,n,1):
    a.append(int(input('digite um valor:')))
print ('Vidas: %d' %somavida(a,e,s))

















