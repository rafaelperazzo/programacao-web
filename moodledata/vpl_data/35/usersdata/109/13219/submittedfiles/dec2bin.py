# -*- coding: utf-8 -*-
from __future__ import division

p=input('Digite o valor de p:')
q=input('Digite o valor de q:')
cont1=0
cont2=0
c=p

while c>=1:
    c=c/10
    cont1=cont1+1
    
o=(cont1*10)

while True:
    if q%o==p:
       print ('S')
    q=q//10
    if q<p:
        print ('N')
       
       