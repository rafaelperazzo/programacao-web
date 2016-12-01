# -*- coding: utf-8 -*-
from __future__ import division

def somavida(p,pe,ps):
    i=pe
    soma=0
    while i<=ps:
        soma=soma+p[i]
        i=i+1
    return soma

p=input('qnt de sala:')
pe=input('porta de entrada:')
ps=input('porta de saida:')
a=[]
for i in range(0,p,1):
    print ('porta %d' %(i+1))
    a.append(int(input('digite um valor:')))
print ('Vidas: %d' %somavida(a,pe,ps))

















