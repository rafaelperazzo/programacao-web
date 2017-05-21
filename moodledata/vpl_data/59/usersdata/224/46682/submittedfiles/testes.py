# -*- coding: utf-8 -*-
import math
n=int(input('Digite n: '))
a=int(input('Digite a: '))
b=int(input('Digite b: '))
mult=1
cont=0
while cont<=n:
    if mult%a==0 or mult%b==0:
        print(mult)
        cont=cont+1
    mult=mult+1
   