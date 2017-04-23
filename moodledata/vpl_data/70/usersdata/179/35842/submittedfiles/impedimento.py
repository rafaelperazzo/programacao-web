# -*- coding: utf-8 -*-
L=float(input('jogador que lança a bola'))
R=float(input('jogador que recebe a bola'))
D=float(input('ultimo jogador defensor'))
if R>50 and L<R and R>D:
    print('S')
else:
    print('N')
