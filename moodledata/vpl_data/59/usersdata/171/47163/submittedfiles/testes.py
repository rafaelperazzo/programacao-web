# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite n:'))
cont=0
atual=n
for i in range(2,n+1,1):
    x=int(input('digite numero:'))
    proximo=x
    if atual==proximo:
        cont=cont+1
print(cont)