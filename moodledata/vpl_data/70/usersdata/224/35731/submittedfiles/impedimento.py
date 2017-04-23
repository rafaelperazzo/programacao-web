# -*- coding: utf-8 -*-
import math
L=int(input('Onde o jogador lança a bola: '))
R=int(input('Onde o jogador recebe a bola: '))
D=int(input('Onde o jogador de defesa estar: '))
if R>L and R>50 and R>D:
    print('Há impedimento')
else:
    print('N')