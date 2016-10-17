# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
#ENTRADA
n=input('insira um numero:')
pi=0
a=1
i=1
j=0
#PROCESSAMENTO
while i<=n:
    if(i%2==0):
        pi=pi-1/(a*(3**j))
    else:
        pi=pi+1/(a*(3**j))
    j=j+1
    a=a+2
    i=i+1
pi=pi*(12**0.5)    
print(' %.6f' %pi)
