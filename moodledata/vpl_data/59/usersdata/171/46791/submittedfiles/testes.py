# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite a quantidade de multiplos a serem mostrados:'))
a=int(input('digite o numero:'))
b=int(input('digite o numero:'))
i=1
for i in range(1,n+4,1):
    if i%a==0 or i%b==0:
        print(i)