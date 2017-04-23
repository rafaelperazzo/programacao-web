# -*- coding: utf-8 -*-
L=float(input('jogador que lança a bola'))
R=float(input('jogador que recebe a bola'))
D=float(input('ultimo jogador defensor'))
S=havera impedimento
N=nao havera impedimento
if R>50 and L<R and R>D:
    print('S')
elif R<50 and L>R and R<D:
    print('N')
