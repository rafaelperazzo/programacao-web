# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
L=int(input('posiçao do q lança a bola:'))
R=int(input('posição do que recebe a bola:'))
D=int(input('ultimo marcador:'))
if R>50 and L<R and R>D:
    print('S')
else:
    print('N')
    