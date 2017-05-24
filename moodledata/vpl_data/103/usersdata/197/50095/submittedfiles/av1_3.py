# -*- coding: utf-8 -*-
import math
a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))
cont=0
resto=0
while resto>0:
    resto=a%b
    cont=cont+1
    b=b%resto
    print(cont)