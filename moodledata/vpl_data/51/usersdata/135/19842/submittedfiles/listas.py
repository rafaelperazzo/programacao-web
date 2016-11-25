# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    cont=0
    for k in range(1,len(lista)-1,1):
        if l[k-1]<l[k]>l[k+1]:
            cont=cont+1
        if l[0]>l[1] or l[-1]>l[-2]:
            cont=cont+4
        if cont==1:
            return True
        else:
            return False
n=input("Entre com a quantidade de termos: ")
l=[]
for k in range(0,n,1):
    l.append(input("Digite o elemento: "))
if pico(l):
    print "S"
else:
    print "N"