# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite a quantidade de multiplos a serem mostrados:'))
for i in range(1,n+1,1):
    if i%2!=0:
        print(i)