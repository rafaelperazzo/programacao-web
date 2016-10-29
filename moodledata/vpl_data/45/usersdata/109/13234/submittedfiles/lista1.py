# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite o valor de n:')
cont1=0
cont2=0
cont3=0
cont4=0

for i in range (0,n,1):
    n1=input('Digite um número:')
    if n1%2==0:
        cont1=cont1+1 
        cont2=cont2+n1
    else:
        cont3=cont3+1
        cont4=cont4+n1
        
print (cont4)
print (cont2)
print (cont3)
print (cont1)
        