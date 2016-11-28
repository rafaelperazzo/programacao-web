# -*- coding: utf-8 -*-
import math

def maiordegrau (a):
    maior=0
    for i in range (0,len (a)-1,1):
        degrau = int(math.fabs  (a [i]- a[i+1]))
        if degrau>maior:
            degrau=maior
    return maior
        
n=int(input("digite a quantidade de termos de a:"))
while n<2:
    n=int(input("digite a quantidade de termos de a:"))
a=[]

for i in range(0,n,1):
    a.append(input("digite a lista:"))
print int(maiordegrau(a))    