# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite a quantidade de pinos da fechadura:')
m=input('Digite a altura para desbloqueio dos pinos:')

a=[]

for i in range (0,n,1):
    a.append(input('Digite a altura de cada pino:'))
    
soma=0
for i in range (0,len(n)-1,1):
    if n[i]!=m:
        x=n[i]-m
        if x<0:
            x=x*(-1)
        else:
            x=x
                
        n[i+1]=n[i+1]+x
        if n[i]==n[i+1]==m:
            soma=soma+x
            i=i+1
        else:
            x=n[i]-m
            if x<0:
                x=x*(-1)
            else:
                x=x
                
            n[i+1]=n[i+1]+x
            n[i+1]=b
            b=b-m
            if b<0:
                b=b*(-1)
            else:
                b=b
                    
            soma=soma+b
                
    else:
        soma=soma+0
            
    
        
                
    

