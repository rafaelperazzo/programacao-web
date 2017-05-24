# -*- coding: utf-8 -*-
import math
n1=int(input('digite n1:'))
n2=int(input('digite n2:'))
cont=0
resto=n1%n2
while resto>0:
    cont=cont+1
    resto==n1%n2
    n1=resto
    n2=n1//n2
print(n1)
print(cont)
