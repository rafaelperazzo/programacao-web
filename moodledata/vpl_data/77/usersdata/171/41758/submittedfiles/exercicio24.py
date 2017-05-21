# -*- coding: utf-8 -*-
import math
n=int(input('digite o valor n1:'))
m=int(input('digite o valor n2:'))
anterior=n
atual=m
resto=anterior%atual
while resto!=0:
    anterior=atual
    atual=resto
    resto=anterior%atual
print('%d'%atual)
