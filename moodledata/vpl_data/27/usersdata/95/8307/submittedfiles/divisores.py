# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('Quantidade de termos:')
a=input('Numero 1:')
b=input('Numero 2:')
i=1
cont=1

while cont<=n:
    if a%i==0 or b%i==0:
        cont=cont+1
        print(i)
    i=i+1
    
    
