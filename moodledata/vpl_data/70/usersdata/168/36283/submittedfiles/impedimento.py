# -*- coding: utf-8 -*-
import math
L=int(input('Digite a posicão do jogador atacante que lança a bola: '))
R=int(input('Digite a posicão do jogador atacante que recebe a bola: '))
D=int(input('Digite a posicão do último jogador defensor: '))
if (R>50) and (L<R) and (R>D):
    print('S')
else:
    print('N')