# -*- coding: utf-8 -*-
from __future__ import division
import math
#COMECE SEU CÓDIGO AQUI

L=input('Digite a posição do jogador L:')
R=input('Digite a posição do jogador R:')
D=input('Digite a posição do jogador D:')

if (R>50) and (L<R) and (R>D):
    print('S')
    
else:
    print('N')