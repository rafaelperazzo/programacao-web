# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Numero de termos: ')

cont=1
soma=0
i=1
    while cont<=n:
        if i%2!=0:
            soma=(i)/(i*i)
        else:
            soma= (i)/-(i*i)
        soma=soma+1
        i=1+1
        cont=cont+1
print soma