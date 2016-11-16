# -*- coding: utf-8 -*-
from __future__ import division

def iguais(lista):
    cont=0
    for i in range (0,len(lista),1):
        if i==0:
            if a[i]==b[i]:
                cont=cont+1
            
        elif i==(len(lista)-1):
            if a[len(lista)-1]==b[len(lista)-1]:
                cont=cont+1
                
        else:
            if a[i]==b[i]:
                cont=cont+1
    
    if cont>0:
        return True
    else:
        return False
        
n=input('Digite a quantidade de termos da lista:')

                    
        

