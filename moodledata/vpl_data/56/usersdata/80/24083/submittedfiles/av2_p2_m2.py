# -*- coding: utf-8 -*-
from __future__ import division

n=int(input('Digite a quantidade de salas:'))
vidas= [""]*n
i=0
while i<n:
    vidas[i]=str(input('Digite a quantidade de vidas:'))
    i=i+1
x=int(input('Digite a porta de entrada:'))    
y=int(input('Digite a porta de saida:'))
a=x-1
b=y-1
print (vidas[a])