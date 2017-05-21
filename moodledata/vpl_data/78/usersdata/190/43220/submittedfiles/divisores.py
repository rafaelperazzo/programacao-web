# -*- coding: utf-8 -*-
import math
n=int(input('digite n: ')
a=int(input('digite a: ')
b=int(input('digite b: ')

multiplo=1
contador=0
while contador<n:
    if (multiplo%a==0) or (multiplo%b==0):
        contador=contador+1
        print(multiplo)
    multiplo=multiplo+1