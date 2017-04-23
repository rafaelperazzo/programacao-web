# -*- coding: utf-8 -*-
import math

P=int(input('digite 0 se for virada para esquerda ou digite 1 se for virada para direita:'))
R=int(input('digite 0 se for virada para esquerda ou digite 1 se for virada para esquerda:'))
if P==1 and R==0:
    print('B')
elif P==0:
    print('C')
else:
    if P==1 and R==1:
        print('A')