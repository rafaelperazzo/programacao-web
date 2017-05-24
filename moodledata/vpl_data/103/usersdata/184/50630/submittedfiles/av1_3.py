# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
resto=a//b
cont=0
i=b
while resto!=0:
    cont=cont+b
    i=i//b
    print(resto)