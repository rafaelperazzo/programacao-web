# -*- coding: utf-8 -*-
import math
l=int(input('Digite a posição de L:'))
r=int(input('Digite a posição de R:'))
d=int(input('Digite a posição de D:'))
if 50<r<100 and l>r and r>d:
    print('S')
else:
    print('N')