# -*- coding: utf-8 -*-
import math
L=float(input('a posição de L:'))
R=float(input('a posição de R:'))
D=float(input('a posição de D:'))
if R>50 and L>R and R>D:
    print('S')
else:
    print('N')