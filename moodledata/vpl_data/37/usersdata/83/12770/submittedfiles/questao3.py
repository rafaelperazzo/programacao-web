# -*- coding: utf-8 -*-
from __future__ import division

p=input('Digite o valor de p: ')
q=input('Digite o valor de q: ')
cont1=0
cont2=0

for i in range (1, p+1, 1) :
    p%p==0
    cont1=cont1+1
for i in range (1, q+1, 1) :
    q%q==0
    cont2=cont2+1
if cont1==1 and cont2==1 :
    if p==q+2 :
        print ('S')
    else :
        print ('N')
else :
    print ('os numeros inseridos não são primos')
    