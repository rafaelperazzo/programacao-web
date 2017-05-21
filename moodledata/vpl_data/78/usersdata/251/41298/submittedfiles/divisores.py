# -*- coding: utf-8 -*-
import math
n = int(input('Digite o numero de divisores: '))
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))

for multiplo in range (1,n+1,1):
    if (multiplo%a==0) or (multiplo%b==0):
        print (multiplo)
