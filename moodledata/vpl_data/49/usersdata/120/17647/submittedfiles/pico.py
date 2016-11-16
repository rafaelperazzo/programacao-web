# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    n=int(input('digite n:'))
    
    anterior=int(input('digite um numero:'))
    atual=int(input('digite um numero:'))
    
    no_picos=0
    no_vales=0
        i=2
    while i<n:
        prox=int(input('digite um numero:'))
        
        if anterior<atual>prox:
        no_picos+=1
        elif anterior>atual<prox:
            no_vales+=1
            
       anterior=atual
       atual=prox
    if no picos==1 and no_vales+0   
    print('S')
    else:
        print('N')
        
    
   