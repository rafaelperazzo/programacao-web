# -*- coding: utf-8 -*-
from __future__ import division
def feliz(a):
    while b!=1:
        soma=0
        for i in range(0,len(a),1):
            soma=soma+(a[i])**2
            b=soma
            if b==1:
                return True
            else:
                return False
                
n=int(input('Digite Valor:'))
a=[]
for i in range(0,n,1):
    v=int(input('digite os elementos:'))
    a.append(v)
if feliz(a):
    print('FELIZ')
else:
    print('NÃO FELIZ')