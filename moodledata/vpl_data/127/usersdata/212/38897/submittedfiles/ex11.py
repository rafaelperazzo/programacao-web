# -*- coding: utf-8 -*-
dia1=int(input('digite o dia da data 1:'))
mes1=int(input('digite o mês da data 1:'))
ano1=int(input('digite o ano da data 1:'))
dia2=int(input('digite o dia da data 2:'))
mes2=int(input('digite o mês da data 2:'))
ano2=int(input('digite o ano da data 2:'))
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