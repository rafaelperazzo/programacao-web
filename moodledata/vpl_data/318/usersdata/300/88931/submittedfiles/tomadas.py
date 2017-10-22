# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO AQUI
T1 = int(input('Digite o valor de T1: '))
T2 = int(input('Digite o valor de T2: '))
T3 = int(input('Digite o valor de T3: '))
T4 = int(input('Digite o valor de T4: '))
while (True):
    if T1 > 1 and T2 > 1 and T3 > 1 and T4 > 1:
        T = (T1-1)+(T2-1)+(T3-1)+T4
        print (T)
        break
    else:
        T1 = int(input('Digite o valor de T1: '))
        T2 = int(input('Digite o valor de T2: '))
        T3 = int(input('Digite o valor de T3: '))
        T4 = int(input('Digite o valor de T4: '))
        