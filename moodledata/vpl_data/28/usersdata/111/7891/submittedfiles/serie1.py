# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Numero de termos: ')

cont=1
soma=0
i=1
while cont<=n:
    if i%2!=0:
        soma=soma + ((i)/(i*i))
    else:
        soma=soma + ((i)/-(i*i))
    i=i+1
    cont=cont+1
print ("%.5f" %soma)