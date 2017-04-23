# -*- coding: utf-8 -*-
A1=int(input('digite ano um:'))
A2=int(input('digite ano dois:'))
M1=int(input('digite mes um:'))
M2=int(input('digite mes dois:'))
D1=int(input('digite dia um:'))
D2=int(input('digite dia dois:'))
if A1>A2:
    print('DATA 1')
elif A1<A2:
    print('DATA 2')
else:
    if M1>M2:
        print('DATA 1')
    elif M1<M2:
        print('DATA 2')
    else:
        if D1>D2:
            print ('DATA 1')
        elif D1<D2:
            print('DATA 2')
        else:
            print('IGUAIS')