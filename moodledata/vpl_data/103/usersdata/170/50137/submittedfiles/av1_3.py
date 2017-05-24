# -*- coding: utf-8 -*-
import math
a=int(input('Digite a:'))
b=int(input('Digite b:'))
ant=a
atual=b
resto=ant%atual
while resto!=0:
    ant=atual
    atual=resto
    resto=ant%atual
print(resto)