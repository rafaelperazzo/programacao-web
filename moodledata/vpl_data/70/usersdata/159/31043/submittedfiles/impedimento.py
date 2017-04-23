# -*- coding: utf-8 -*-
import math
L=int(input('Posição do atacante que lança a bola:'))
R=int(input('Posição do atacante que rebate a bola:'))
D=int(input('Posição do último jogador defensor:'))
if R>50 and L<R and R>D:
    print('S')
else:
    print('N')