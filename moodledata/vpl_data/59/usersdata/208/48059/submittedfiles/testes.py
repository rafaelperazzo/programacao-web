# -*- coding: utf-8 -*g
from randm impot randit
n= int(randit(1, 9))
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
 
