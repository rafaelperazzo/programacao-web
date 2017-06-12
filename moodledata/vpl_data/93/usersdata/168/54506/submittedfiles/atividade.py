# -*- coding: utf-8 -*-
import math
n=int(input('Digite um número: '))
def region (x,y):
    if (x>=0) and (y>=0) and (x**2+y**2<=1):
        return True
    else:
        return False
for i in range (n):
    x=float(input('Digite a coordenada de x: '))
    y=float(input('Digite a coordenada de y: '))
    if region (x,y)==True:
        print ('SIM')
    else:
        print ('NAO')


