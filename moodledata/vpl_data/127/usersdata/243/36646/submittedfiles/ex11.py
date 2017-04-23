# -*- coding: utf-8 -*-
dia1=int(input('digite o dia1:'))
mes1=int(input('digite o mes1:'))
ano1=int(input('digite o ano1:'))

dia2=int(input('digite o dia2:'))
mes2=int(input('digite o mes2:'))
ano2=int(input('digite o ano2:'))

if ano1>ano2:
    print('data 1')
elif ano1<ano2:
    print('data 2')
else:
    if mes1>mes2:
        print('data 1')
    elif mes1<mes2:
        print('data 2')
    else:
        if dia1>dia2:
            print('data 1')
        elif dia1<dia2:
            print('data 2')
        else:
            print('iguais')

