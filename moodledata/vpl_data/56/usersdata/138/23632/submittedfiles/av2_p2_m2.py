# -*- coding: utf-8 -*-
from __future__ import division

def soma(a):
    i=0
    b=[]
    soma=0
    while i<=len(a):
        soma=soma+a[i]
        b.append(soma)
        i=i+1
    return b

def maior(b,ent,saida):
    for i in range(0,len(b),1):
        if b[i]>b[i+1]:
            maior = b[i]
        if b[i]>maior:
            maior=b[i]
    return maior
    
n=input('n:')
ent=input('ent:')
saida=input('saida:')
a=[]
for i in range(0,len(a),1):
    a.append(int(input('digite um valor:'))
c=maior(b,ent,saida)
print c














