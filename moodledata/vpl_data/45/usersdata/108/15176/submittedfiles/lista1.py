# -*- coding: utf-8 -*-
from __future__ import division

n= input ('Digite n:')
l = []
contadorpar=0
contadorimpar=0
somatoriopar=0
somatorioimpar=0

for i in range (0,n,1):
    l.append (input ('Digite um elemento:'))
    
    if ((l[i]%2)==0):
        contadorpar=contadorpar+1
        somatoriopar=somatoriopar+l[i]
        
    else:
        contadorimpar=contadorimpar+1
        somatorioimpar=somatorioimpar+l[i]
        
print (somatorioimpar)
print (somatoriopar)
print (contadorimpar)
print (contadorpar)
print (l)