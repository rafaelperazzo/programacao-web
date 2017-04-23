# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
L=float(input('Posição do jogador lançador: '))
R=float(input('Posição do jogador que recebe a bola: '))
D=float(input('Posição do último jogador defensor: '))
if R>50 and L<R and R>D:
    print('S')
else:
    print('N')