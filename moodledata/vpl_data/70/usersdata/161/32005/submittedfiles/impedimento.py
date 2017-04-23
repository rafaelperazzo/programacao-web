# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
L=int(input('Informe a posição do jogador L:'))
R=int(input('Informe a posição do jogador R:'))
D=int(input('Informe a posição do jogador D:'))
if L>100:
    L/10
if R>100:
    R/10
if D>100:
    D/10
if R>50 and L<R and R<D:
    print('S')
else:
    print('N')