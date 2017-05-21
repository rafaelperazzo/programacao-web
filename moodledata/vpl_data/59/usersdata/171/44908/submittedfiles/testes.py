# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite um dado numero n:'))
i=2
contador=0
while n-1>i:
    n%i==0
    contador=contador+1
    i=i+1
if contador==0:
    print('É PRIMO')
else:
    print('NAO É PRIMO')