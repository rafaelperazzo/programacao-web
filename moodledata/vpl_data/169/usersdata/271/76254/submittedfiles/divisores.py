# -*- coding: utf-8 -*-
import math
#ENTRADA
n = int(input('Digite o numero de multiplos : '))
a = int(input('Digite o valor de a : '))
b = int(input('Digite o valor de b : '))
c = 1
cont = 0
while (cont<n) :
    if (c%a) == 0 or (c%b) == 0 :
        print(c)
        c = c+1
        cont = cont+1
    else :
        c = c+1
            
            


