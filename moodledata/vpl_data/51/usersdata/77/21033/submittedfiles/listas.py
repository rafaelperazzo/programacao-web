# -*- coding: utf-8 -*-
from __future__ import division
import math

def maiorDegrau(a):
    maior=0
    for i in range(0,len(a)-1,1):
        degrau= math.fabs(a[i]-a[i+1])
        if degrau>maior:
            maior=degrau
        
    return maior
        

n=int(input('Digite a quantidade de termos da lista:'))

a=[]

for i in range(0,n,1):
    


