# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO


def somaLinhas(a):
    b=[]
    
    for i in range(0,a.shape[0],1):
        soma=0
        
        for j in range(0, a.shape[1], 1):
            soma = soma + a[i,j]
            
            b.append(a[i,j])
    return b
        

        