# -*- coding: utf-8 -*-
import math
L=int(input('jogador que lança a bola'))
R=int(input('jogador que recebe a bola'))
D=int(input('ultimo jogador defensor'))
if R>50 and L<R and R>D:
    print('S')
elif R<50 and L>R and R<D:
    print('N')
