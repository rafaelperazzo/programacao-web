# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO AQUI
while(True):
    t1 = int(input('Digite o número de tomadas da T1'))
    t2 = int(input('Digite o número de tomadas da T2'))
    t3 = int(input('Digite o número de tomadas da T3'))
    t4 = int(input('Digite o número de tomadas da T4'))
    if t1 > 0 and t2 > 0 and t3 > 0 and t4 > 0:
        n = t1 + (t2-1) + (t3-1) + (t4-1)
        print(n)
        break
    else:
        print('O NÚMERO DE TOMADAS TEM QUE SER MAIOR QUE 0, DIGITE NOVAMENTE:\n')


