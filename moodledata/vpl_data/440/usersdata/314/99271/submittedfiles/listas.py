# -*- coding: utf-8 -*-
import math
def degrau(lista):
    primeiro=nu[0]
    
    for i in range(0,len(nu),1):
        diferenca=primeiro-nu[i]
       
    print ( math.fabs(diferenca))




n=int(input('Digite n: '))
if n>=2:
    nu=[]
    for i in range(0,n,1):
        nu.append(int(input('Digite elementos da lista: ')))

print(degrau(nu))        
