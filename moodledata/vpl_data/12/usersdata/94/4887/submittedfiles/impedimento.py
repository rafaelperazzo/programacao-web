# -*- coding: utf-8 -*-
from __future__ import division
import math
#COMECE SEU CÓDIGO AQUI

L=input('indique a posiçao de L:')
R=input('indique a posiçao de R:')
D=input('indique a posiçao de D:')

if R>50 and L<R and R>D:
    print('impedimento')

else:
    print('nao impedido')