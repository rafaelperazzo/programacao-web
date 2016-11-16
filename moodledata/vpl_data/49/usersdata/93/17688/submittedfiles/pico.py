# -*- coding: utf-8 -*-
from __future__ import division

def pico(a):
    #CONTINUE...
    if a[1]<=a[0]:
        return 'N'
    maior=0
    for i in range(0,len(a),1):
        maior=a[i]
        if i==len(a)-1:
            return 'N'
            break
        if a[i+1]<=a[i]:
            break
    print(i)
        

print(pico(a))
        
        
    
    


n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
