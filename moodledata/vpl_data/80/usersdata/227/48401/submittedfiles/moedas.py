# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('valor da moeda:'))
b=int(input('valor da moeda:'))
c=int(input('valor da cedula:'))

cont=0
quantidadeA=c//a
quantidadeB=0

while quantidadeA>0:
    troco=c-quantidadeA*a
    if troco%b==0:
        quantidadeB=c//b
        cont=cont+1
        
    else:
        quantidadeA=quantidadeA-1
if cont>0:
    print quantidadeA
    print qunatidadeB
    
else:
     'N'