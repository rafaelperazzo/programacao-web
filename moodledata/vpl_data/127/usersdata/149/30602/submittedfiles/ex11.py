# -*- coding: utf-8 -*-
x1=input('digite o nome:')
x2=input('digite o nome:')
D1=int(input('digite o dia de nascimento de ' + x1 + ': '))
M1=int(input('digite o mês do nascimento da ' + x1 + ':'))
A1=int(input('digite o ano do nascimento da ' + x1 + ':'))
D2=int(input('digite o dia do nascimento da ' + x2 + ':'))
M2=int(input('digite o mês do nascimento da ' + x2 + ':'))
A2=int(input('digite o ano do nascimento da ' + x2 + ':'))
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
            print(x1 + " tem a mesma idade de " + x2)

