# -*- coding: utf-8 -*-
import math
N=int(input('Digite o valor de N:'))
contador=1
while contador<=N:
    A=float(input('Digite o valor de A:'))
    B=float(input('Digite o valor de B:'))
    if A>=0 and B>=0 and ((A**2)+(B**2))<=1:
        print('SIM')
    else:
        print('NÃO')
    contador=contador+1

