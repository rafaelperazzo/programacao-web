# -*- coding: utf-8 -*-
import math
n=int(input('digite n'))
m=int(input('digite m'))
anterior==n
atual==m
resto==anterior%atual
while resto!=0:
    anterior==atual
    atual==resto
    resto==anterior%atual
print('%d'%resto)