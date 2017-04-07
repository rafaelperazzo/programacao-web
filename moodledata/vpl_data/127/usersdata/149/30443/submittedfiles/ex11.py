# -*- coding: utf-8 -*-
x1=input('digite o nome:')
x2=input('digite o nome:')
D1=int(input('digite o dia de nascimento de ' + x1 + ': '))
M1=int(input('digite o mês do nascimento da pessoa 1:'))
A1=int(input('digite o ano do nascimento da pessoa 1:'))
D2=int(input('digite o dia do nascimento da pessoa 2:'))
M2=int(input('digite o mês do nascimento da pessoa 2:'))
A2=int(input('digite o ano do nascimento da pessoa 2:'))
if A1>A2:
    print(x1)
elif A1<A2:
    print(x2)
else:
    if M1>M2:
        print('pessoa 1 é mais nova')
    elif M1<M2:
        print('pessoa 2 é mais nova')
    else:
        if D1>D2:
            print('pessoa 1 é mais nova')
        elif D1<D2:
            print('pessoa 2 é mais nova')
        else:
            print('a duas têm a mesma idade')

