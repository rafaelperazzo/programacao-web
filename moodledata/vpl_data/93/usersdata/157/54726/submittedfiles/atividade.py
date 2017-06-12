# -*- coding: utf-8 -*-
import math
n=int(input('Digite o valor: '))

def region (x,y):
    if x>=0 and y>=0 and x**2+y**2<=1:
        return True 
    else:
        return False
for i in range (n):
    x=float(input('Digite o valor da Abscissa X: '))
    y=floar(input('Digite o valor da Ordenada Y: '))
    if region (x,y) == True:
        print('Sim')
    else:
        print('Nao')