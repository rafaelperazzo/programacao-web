# -*- coding: utf-8 -*-
from __future__ import division

def somavida(a,b,c):
    i=0
    soma=0
    while b<=c:
        soma=soma+a[i]
        i=i+1
    return soma
'''
def maiorlista(b,ent,saida):
    for i in range(0,len(b),1):
        if b[i]>b[i+1]:
            maior = b[i]
        if b[i]>maior:
            maior=b[i]
    return maior
'''

p=input('qnt de sala:')
n=input('porta de entrada:')
q=input('porta de saida:')
a=[]
for i in range(0,n,1):
    a.append(int(input('digite um valor:'))

print ('%d' %somavida(p,n,q))















