# -*- coding: utf-8 -*-
from __future__ import division

def maior_degrau(x):
    maior=0
    for i in range(0,len(x)-1,1):
        degrau=math.fabs(x[i]-x[i+1])
        if degrau>maior:
            maior=degrau
    
    return maior

n=input('Digite a quantidade de termos de a:')
while n<2:
    n=input('Digite a quantidade de termos de a:')
a=[]

for i in range(0,n,1):
    a.append(input('Digite um valor para a:'))
    
print maior_degrau(a)