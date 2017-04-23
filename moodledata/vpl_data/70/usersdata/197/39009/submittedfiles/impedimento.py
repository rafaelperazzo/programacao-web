# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
L=float(input('Digite a posição do jogador L:'))
R=float(input('Digite a posição do jogador R:'))
D=float(input('Digite a posição do jogador D:'))
if R>50 and L<R and R>D:
    print('S')
    
else:
    print('N')