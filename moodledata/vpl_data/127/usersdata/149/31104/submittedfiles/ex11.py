# -*- coding: utf-8 -*-
D1=int(input('digite o dia de nascimento :'))
M1=int(input('digite o mês do nascimento :'))
A1=int(input('digite o ano do nascimento :'))
D2=int(input('digite o dia do nascimento :'))
M2=int(input('digite o mês do nascimento :'))
A2=int(input('digite o ano do nascimento :'))
if A1>A2:
    print('pessoa 1')
elif A1<A2:
    print('pessoa 2')
else:
    if M1>M2:
        print('pessoa 1')
    elif M1<M2:
        print('pessoa 2')
    else:
        if D1>D2:
            print('pessoa 1')
        elif D1<D2:
            print('pessoa 2')
        else:
            print('iguais')

