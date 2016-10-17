# -*- coding: utf-8 -*-
from __future__ import division
import math
x=input('Digite um número real: ')
y=input('Digite um número real: ')
anterior=x
atual=y
resto=(anterior%atual)
cont=1
while resto!=0:
    anterior=atual
    atual=resto
    c=cont+1
    if resto!=0:
        resto=(anterior%atual)

    print c
    