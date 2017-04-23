# -*- coding: utf-8 -*-
D1=int(input('digite o dia da data 1:'))
D2=int(input('digite o dia da data 2:'))
M1=int(input('digite o mês da data 1:'))
M2=int(input('digite o mês da data 2:'))
A1=int(input('digite o ano da data 1:'))
A2=int(input('digite o ano da data 2:'))
if A1>A2:
    print('data1')
elif A2>A1:
    print('data2')
else:
    if M1>M2:
        print('data1')
    elif M2>M1:
        print('data2')
    else:
        if D1>D2:
            print('data1')
        elif D2>D1:
            print('data2')
        else:
            print('iguais')