# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
L=int(input('Informe a posição do jogador L entre 0 e 100:'))
R=int(input('Informe a posição do jogador R entre 0 e 100:'))
D=int(input('Informe a posição do jogador D entre 0 e 100:'))
0<=L<=100
0<=R<=100
0<=D<=100
if R>50 and L<R and R<D:
    print('S')
else:
    print('N')