# -*- coding: utf-8 -*-
import math

def maiorDegrau(a):
    maior=0
    for i in range (0,len(a)-1,1):
        degrau=math.fabs(a[i]-a[i+1])
        if degrau>maior:
            maior=degrau
            
    return maior 
    
                
n=int(input('Digite a quantidade de termos da lista:'))

while n<2:
    n=int(input('Digite a quantidade de termos da lista:'))
    
a=[]

for i in range (0,n,1):
    a.append(input('Digite os elementos da lista:'))
    
print maiorDegrau(a)

    
    

    
            
    
            
 

