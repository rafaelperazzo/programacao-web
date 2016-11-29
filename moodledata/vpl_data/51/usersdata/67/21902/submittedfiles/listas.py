# -*- coding: utf-8 -*-
from __future__ import division

def degrau (a):
    degraur=0
    for i in range (0,len(a)-1,1):
        if a[i]-a[i+1]>degraur:
            degraur=a[i]-a[i+1]
    return degraur
        

n=input("Digite a quantia de termos:")
a=[]

for i in range (0,n,1):
    a.append(input("Digite um termo para a:"))

print ("%d" %degrau(a))