# -*- coding: utf-8 -*-
from __future__ import division

qs=input('Quantidade de salas:')

for i in range (0,qs,1):
    sala=[]
    sala.append(input('quantidade de vidas da sala:'))

pe=input('porta de entrada:')
ps=input('porta de saída:')
    
soma=0
for j in range(pe,ps+1,1):
    a=sala[j]
    print sala[j]
    soma=soma+a
   
        
print soma