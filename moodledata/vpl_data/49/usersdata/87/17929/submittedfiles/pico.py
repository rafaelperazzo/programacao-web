# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    cont=0
    for i in range (0,len(lista),1):
        if i==0:
            if lista[i]>lista[i+1]:
                cont=cont+1
                break
            if lista[i+1]<lista[i]:
                cont=cont+1
            return True
        else:
            return False

a=[]
n=input("digite valor da quantidade de elementos:")
for i in range (0,n,1):
    a.append(input('digite elementos:'))

if pico(a):
    print("S")
else:
    print("N")
