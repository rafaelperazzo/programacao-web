# -*- coding: utf-8 -*-
import numpy as np

n=int(input('Dimensão da matriz:'))
a=np.zeros((n,n))
x=int(input('Digite o indice da linha em que a peça esta:'))
y=int(input('Dimgite o indice da coluna em que a peça esta:'))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]= input('Digite o número')

somalinha=0
somacoluna=0

for i in range (0,a.shape[1],1):
        somalinha=somalinha + a[x,i]
    
for i in range (0,a.shape[0],1):
    somacoluna=somacoluna + a[i,y]
            
peso= somalinha+somacoluna - 2*a[x,y]
print(peso)











