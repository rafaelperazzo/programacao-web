# -*- coding: utf-8 -*-
from __future__ import division

def maiordegrau (a):
    maior=0
    for i in range (0,len (a)-1,1):
        degrau = math.fabs  (a [i]- a[i+1])
        if degrau>maior:
            degrau+maior
    return maior
        
n=input("digite a quantidade de termos de a:")
a=[]
for i in range(0,n,1):
    a.append(input("digite a lista:")
print int  (maiordegrau (a))    