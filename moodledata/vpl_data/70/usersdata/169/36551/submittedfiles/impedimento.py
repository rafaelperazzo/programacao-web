# -*- coding: utf-8 -*-
import math
L=int(input('Digite a Posição do Jogador L:'))
R=int(input('Digite a Posição do Jogador R:'))
D=int(input('Digite a Posição do Jogador D:'))
if (R>50) and (L<R) and (R>D):
    print ('S')
else:
    print('N')