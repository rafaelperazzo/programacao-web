# -*- coding: utf-8 -*-
import math
L=float(input('escreva a posição de L:'))
R=float(input('escreva a posição R:'))
D=float(input('escreva a posição D:'))

if R>50 and L<R and R>D:
    print('S')
else:
    print('N')