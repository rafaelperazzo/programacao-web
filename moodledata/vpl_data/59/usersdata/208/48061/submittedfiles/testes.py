# -*- coding: utf-8 -*g
from random import randint
n= int(randint(1, 9))
p=0
t=0 
while p != n:
    p=int(input('seu palpite:'))
    t += 1
    if p==n:
        print('acertou! placar %i'%t)
    elif p<n:
        print('chue um valor maior')
    else:
        print('chute um valor menor')
print('fim de jogo')
 
