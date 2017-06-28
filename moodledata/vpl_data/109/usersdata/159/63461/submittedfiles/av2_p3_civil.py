# -*- coding: utf-8 -*-
import numpy as np

def pesos (a,x,y):
    verticais=[]
    horizontais=[]
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if j==y:
                verticais.append(a[i,j])
            if i==x:
                horizontais.append(a[i,j])
    peso1=0
    peso2=0
    
    for i in range (0,len(verticais),1):
        peso1=peso1+verticais[i]
    for i in range (0,len(horizontais),1):
        peso2=peso2+horizontais[i]
    
    peso1=peso1-a[x,y]
    peso2=peso2-a[x,y]
    pesotot=peso1+peso2
    return pesotot
    

