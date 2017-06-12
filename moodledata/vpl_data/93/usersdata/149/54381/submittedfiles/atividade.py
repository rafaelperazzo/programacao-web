# -*- coding: utf-8 -*-
import math
n=int(input('digite um número'))

def regiao(x,y):
    if (x>=0) and (y>=0) and (x**2+y**2<=1):
        return True 
    else:
        return False
for i in range(n):
    x=float(input('digite a coordenada de x: ' )
    y=float(input('digite a coodernada de y: ' )
    if region(x,y)==True:
        print('SIM')
    else:
        print('NAO')


