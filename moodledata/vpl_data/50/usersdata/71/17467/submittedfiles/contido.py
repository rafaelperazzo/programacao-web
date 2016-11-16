# -*- coding: utf-8 -*-
from __future__ import division

def qiguais(listax,listay):
    igual=0
    for i in range(0,len(listax),1):
        if listax[i] in listay:
            igual=igual+1
    return igual
n=input("Insira a quantidade de elementos da lista X: ")
m=input("Insira a quantidade de elementos da lista Y: ")
x=[]
y=[]
for i in range(0,n,1):
    x.append(input("Insira um elemento na lista X: "))
for j in range(0,n,1):
    y.append(input("Insira um elemento na lista Y: "))
print qiguais(x,y)