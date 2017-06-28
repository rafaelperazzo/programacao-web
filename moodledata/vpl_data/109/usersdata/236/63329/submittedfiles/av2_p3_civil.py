# -*- coding: utf-8 -*-
import numpy as np

def matriz(a):
    n=int(input('Dimensão da matriz:'))
    a=np.zeros((n,n))
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            a[i,j]= input('Digite o número')
def peso(x,y):
    somalinha=0
    somacoluna=0
    for i in range (x):
        for j in range (0,a.shape[1],1):
            somalinha=somalinha + a[x,y]
    
    for j in range (y):
        for i in range (0,a.shape[0],1):
            somacoluna=somacoluna + a[x,y]
            
    peso= somalinha+somacoluna - 2*a[x,y]

    
        
    



x=int(input('Digite o indice da linha em que a peça esta:'))
y=int(input('Dimgite o indice da coluna em que a peça esta:'))







