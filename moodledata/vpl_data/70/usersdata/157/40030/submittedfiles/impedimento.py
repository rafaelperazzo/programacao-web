# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
l=int(input('Diga qual a posição de L:'))
r=int(input('Diga qual a posição de R:'))
d=int(input('Diga qual a posição de D:'))
if r>50 and l<r and r>d:
    print('S')
else:
    print('N')