# -*- coding: utf-8 -*-
import math
n=int(input('Digite n:'))
a=int(input('Digite a:'))
b=int(input('Digite b:'))

contador=0
i=1

while contador<n:
    if i%a==0 or i%b==0:
        print(i)
        contador=contador+1
    i=i+1
    