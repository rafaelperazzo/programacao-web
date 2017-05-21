# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite n:'))
cont=0
for i in range(1,n+1,1):
    x=int(input('digite numero:'))
    if x==x:
        cont=cont+1
    print(cont)