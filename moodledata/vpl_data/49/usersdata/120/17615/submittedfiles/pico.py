# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    n=int(input('digite n:'))
    anterior=int(input('digite um numero:'))
    atual=int(input('digite um numero:'))
    if anterior< atual:
        pico=True
        subida=True
    else:
        pico= False
    anterior=atual
    i=2
    while i<n:
        atual=int(input('digite um numero:')
        
        if anterior< atual:
            if not subida:
                pico=False
        else:
            subida=False
            
        anterior=atual
        i+=1
        
    if subida:
        pico=False
        
    if pico:
        print('S')
    else:
        print('N')
        
    
   