# -*- coding: utf-8 -*-
import math
n=int(input('digite n'))
m=int(input('digite m'))
anterior=n
atual=m
resto=atual%anterior
while resto!=0:
    anterior=atual
    atual=resto
    resto=atual%anterior
print('%d'%resto)