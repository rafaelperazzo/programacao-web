# -*- coding: utf-8 -*-
from __future__ import division
import math


def maiorDegrau(l):
    maior=0
    for i in range(0,len(l)-1,1):
        degrau= math.fabs(l[i]-l[i+1])
        if degrau>maior:
            maior=degrau
        
    return maior

n=input("Digite o valor de n: ")
l=[]

for i in range(0,n,1):
    l.append(input("Digite um elemnto: "))
    
print ("%.d"%maiorDegrau(l))