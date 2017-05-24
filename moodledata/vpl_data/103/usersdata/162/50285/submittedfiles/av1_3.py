# -*- coding: utf-8 -*-
import math
a=int(input('Digite o primeiro número:'))
b=int(input('Digite o segundo número:'))
ant=a
atual=b
resto=ant%atual
while resto!=0:
    post=atual
    atual=resto
    resto=resto+1
print(resto)    
