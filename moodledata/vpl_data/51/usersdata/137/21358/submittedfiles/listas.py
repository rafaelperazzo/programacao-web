# -*- coding: utf-8 -*-
from __future__ import division
def degrau (lista):
    a=[]
    for i in range (0,len(lista)-1,1):
        b=lista[i+1]-lista[i]
        if b<0:
            b=(-1)*b
        a.append(b)
    return a
def maiorDegrau(s):
    maior=0
    for i in range (0,len(s)-1,1):
        if s[i]>s[i+1]:
            maior=s[i]
        if maior<s[i+1]:
            maior=s[i+1]
        return maior
         

n=input('n:')
lista=[]
for i in range (0,n,1):
    lista.append(input('lista:'))
s=degrau(lista)
m=maiorDegrau(s)
print m
        