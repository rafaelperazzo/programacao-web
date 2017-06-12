# -*- coding: utf-8 -*-
import math
n=int(input('Digite valor de n: '))
def regiao(x,y):
    if (x>=0) and (y>=0) and ((x**2+y**2)<=1):
        return True
    else:
        return False
for i in range(n):
    x=float(input('Digite coordenada x: '))
    y=float(input('Digite coordenada y: '))
    if regiao(x,y)==True:
        print('SIM')
    else:
        print('NAO')

