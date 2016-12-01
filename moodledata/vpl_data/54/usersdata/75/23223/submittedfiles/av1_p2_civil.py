# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite a quantidade de pinos da fechadura:')
m=input('Digite a altura para desbloqueio dos pinos:')

a=[]

for i in range (0,n,1):
    a.append(input('Digite a altura de cada pino:'))
    
soma=0
for i in range (0,len(a)-1,1):
    if a[i]!=m:
        x=a[i]-m
        if x<0:
            x=x*(-1)
        else:
            x=x
                
        a[i+1]=a[i+1]+x
        if a[i]==a[i+1]==m:
            soma=soma+x
            i=i+1
        else:
            x=a[i]-m
            if x<0:
                x=x*(-1)
            else:
                x=x
                
            a[i+1]=a[i+1]+x
            a[i+1]=b
            b=b-m
            if b<0:
                b=b*(-1)
            else:
                b=b
                    
            soma=soma+b
                
    else:
        soma=soma+0
            
    
        
                
    

