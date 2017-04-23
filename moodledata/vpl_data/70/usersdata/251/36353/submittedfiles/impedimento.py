# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
l = int(input('Digite de 0 a 100, a posição do jogador lançador: '))
r = int(input('Digite de 0 a 100, a posição do jogador atacante: '))
d = int(input('Digite de 0 a 100, a posição do último defensor: '))

if r>50  and l<r and r>d:
    print('S')

else:    
    print('N')