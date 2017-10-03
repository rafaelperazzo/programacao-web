# -*- coding: utf-8 -*-
import math
#ENTRADA
n = int(input('Digite o numero de pontos : '))
i = 1
while (i<=n) :
    x = float(input('Digite a coordenada x: '))
    y = float(input('Digite a coordenada y: '))
    if (x>=0) and (y>=0) and ((x*x)*(y*y)<=1) :
        print'SIM'
    else :
        print('NAO')
        



