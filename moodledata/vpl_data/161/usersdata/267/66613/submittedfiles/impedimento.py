# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
L = float(input('Posição do jogador L: '))
R = float(input('Posição do jogador R: '))
D = float(input('Posição do jogador D: '))
if R>50 and L<R and D<R:
    print('S')
else:
    print('N')