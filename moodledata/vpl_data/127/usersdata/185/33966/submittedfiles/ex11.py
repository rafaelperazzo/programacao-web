# -*- coding: utf-8 -*-
D1=int(input('digite dia um:'))
M1=int(input('digite mes um:'))
A1=int(input('digite ano um:'))
D2=int(input('digite dia dois:'))
M2=int(input('digite mes dois:'))
A2=int(input('digite ano dois:'))
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