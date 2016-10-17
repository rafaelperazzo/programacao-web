# -*- coding: utf-8 -*-
from __future__ import division
import math
x=input('Digite um número real: ')
y=input('Digite um número real: ')
anterior=x
atual=y
resto=(anterior%atual)
cont=0
while resto!=0:
    anterior=atual
    atual=resto
    resto=(anterior%atual)
    h=resto
    c=cont+1
    print h
    print c