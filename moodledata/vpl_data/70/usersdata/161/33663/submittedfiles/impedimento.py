# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
L=int(input('Informe a posição do jogador R:'))
R=int(input('Informe a posição do jogador L:'))
D=int(input('Informe a posição do jogador D:'))
if R>50 and L<R and R>D:
    print('S')
else:
    print('N')