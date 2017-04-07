# -*- coding: utf-8 -*-
D1=int(input('digite o dia da pessoa 1:'))
M1=int(input('digite o mês da pessoa 1:'))
A1=int(input('digite o ano da pessoa 1:'))
D2=int(input('digite o dia da pessoa 2:'))
M2=int(input('digite o mês da pessoa 2:'))
A2=int(input('digite o ano da pessoa 2:'))
if A1>A2:
    print('data da pessoa 1:')
elif A1<A2:
    print('data da pessoa 2:')
else: 
    if M1>M2:
        print('pessoa 1:')
    elif M1<M2:
        print('pessoa 2:')
else:
    if D1>D2:
    print('pessoa 1:')
    elif D1<D2:
    print('pessoa 2:')
else:
    print('pessoas iguais')

