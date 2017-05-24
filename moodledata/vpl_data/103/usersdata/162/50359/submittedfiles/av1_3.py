# -*- coding: utf-8 -*-
import math
a=int(input('Digite o primeiro número:'))
b=int(input('Digite o segundo número:'))
ant=a
atual=b
cont=1
resto=ant%atual
while resto!=0:
    post=atual
    atual=resto
    if post%resto==0:
       print(resto)    
        
