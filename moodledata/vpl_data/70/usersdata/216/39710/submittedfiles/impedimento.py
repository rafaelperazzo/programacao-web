# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
L=int(input('Digite a posição de L:'))
R=int(input('Digite a posição de R:'))
D=int(input('Digite a posição de D:'))

if R>50 and L<R and R>D:
    print('S')
else:
    print('N')
