# -*- coding: utf-8 -*-
import math
n=int(input('Digite n: '))
t=n
cont=0
while t>0:
    t=t//10
    cont=cont+1
print(cont)