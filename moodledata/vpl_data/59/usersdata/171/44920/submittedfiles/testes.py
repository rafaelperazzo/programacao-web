# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite um dado numero a:'))
temp=n
cont=n
while temp>0:
    temp=temp//10
    cont=cont+1
print(cont)
   