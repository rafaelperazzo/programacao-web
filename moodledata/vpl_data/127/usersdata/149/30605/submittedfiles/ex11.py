# -*- coding: utf-8 -*-
x1=input('digite o nome da pessoa 1:')
x2=input('digite o nome da pessoa 2:')
D1=int(input('digite o dia de nascimento de ' + x1 + ': '))
M1=int(input('digite o mês do nascimento da ' + x1 + ':'))
A1=int(input('digite o ano do nascimento da ' + x1 + ':'))
D2=int(input('digite o dia do nascimento da ' + x2 + ':'))
M2=int(input('digite o mês do nascimento da ' + x2 + ':'))
A2=int(input('digite o ano do nascimento da ' + x2 + ':'))
if A1>A2:
    print(x1 é mais novo)
elif A1<A2:
    print(x2 é mais novo)
else:
    if M1>M2:
        print(x1 é mais novo)
    elif M1<M2:
        print(x2 é mais novo)
    else:
        if D1>D2:
            print(x1 é mais novo)
        elif D1<D2:
            print(x2 é mais novo)
        else:
            print(x1 + " e tem a mesma idade de " + x2)

