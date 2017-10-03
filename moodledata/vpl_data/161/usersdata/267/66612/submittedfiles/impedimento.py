# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
R = float(input('Posição do jogador R: '))
L = float(input('Posição do jogador L: '))
D = float(input('Posição do jogador D: '))
if R>50 and L<R and D<R:
    print('S')
else:
    print('N')