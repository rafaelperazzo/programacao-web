# -*- coding: utf-8 -*-
from __future__ import division
import math
def maiorDegrau(b):
    maior=0
    for i in range (0,len(b)-1,1):
        degrau=int(math.fabs(b[i]-b[i+1])) #<------------- FALTOU CONVERTER PRA INTEIRO!!
        if degrau>maior:
            maior=degrau
    return maior
    
b=[]
n=input('termos da lista:')
for i in range (0,n,1):
    b.append(input('digite um elemento de b:'))
print maiorDegrau(b)
            
    

