# -*- coding: utf-8 -*-
import math
def degrau(lista):
    primeiro=nu[i]
    diferenca=[]
    for i in range(0,len(nu),1):
        for j in range(i+1,len(nu),1):
            diferenca.append(primeiro-nu[j])
    maior=diferenca[0]
    if diferenca[i]>maior:
        maior=diferenca[i]
    print(math.fabs(maior))    
            





n=int(input('Digite n: '))
if n>=2:
    nu=[]
    for i in range(0,n,1):
        nu.append(int(input('Digite elementos da lista: ')))
    
    
    diferenca=[]
    for i in range(0,len(nu)-1,1):
        diferenca.append(math.fabs(nu[i]-nu[i+1]))
    maior=diferenca[0]
    if diferenca[i]>maior:
        maior=diferenca[i]
    print(math.fabs(maior))      

    
