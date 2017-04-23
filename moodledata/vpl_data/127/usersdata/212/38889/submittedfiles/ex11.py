# -*- coding: utf-8 -*-
dia1=int(input('digite o dia da primeira data:'))
mes1=int(input('digite o mês da primeira data:'))
ano1=int(input('digite o ano da primeira data:'))
dia2=int(input('digite o dia da primeira data:'))
mes2=int(input('digite o mês da primeira data:'))
ano2=int(input('digite o ano da primeira data:'))
if ano1<ano2:
    print('data2')
elif ano1>ano2:
    print('data1')
else:
    if mes1<mes2:
        print('data2')
    elif mes1>mes2:
        print('data1')
    else:
        if dia1<dia2:
            print('data2')
        elif dia1>dia2:
            print('data1')
        else:
            print('iguais')