# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
0<=L<=100
0<=R<=100
0<=D<=100
L=int(input('Informe a posição do jogador L:'))
R=int(input('Informe a posição do jogador R:'))
D=int(input('Informe a posição do jogador D:'))
if R>50 and L<R and R<D:
    print('S')
else:
    print('N')