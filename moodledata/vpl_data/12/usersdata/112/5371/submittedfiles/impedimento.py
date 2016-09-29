# -*- coding: utf-8 -*-
from __future__ import division
import math
#COMECE SEU CÓDIGO AQUI
L=input('Digite a posição em metros de L:')
R=input('Digite a posição em metros de R:')
D=input('Digite a posição em metros de D:')
if R>50 and L<R and R>D:
    print('S')
else: 
    print('N')