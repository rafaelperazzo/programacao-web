# -*- coding: utf-8 -*-
dia1 = int(input('digite o dia da data 1:'))
mes1 = int(input('digite o mês da data 1:'))
ano1 = int(input('digite o ano da data 1:'))
dia2 = int(input('digite o dia da data 2:'))
mes2 = int(input('digite o mês da data 2:'))
ano2 = int(input('digite o ano da data 2:'))
if ano1>ano2  :
    print('DATA 1')
elif ano1=ano2 :
    if mes1>mes2 :
        print('DATA 1')
    elif mes1=mes2 :
        if dia1>dia2 :
            print('DATA 1')
        elif dia1=dia2 :
            print('IGUAIS')
        else :
            print('DATA 2')
    else :
        print('DATA 2')
else :
    print('DATA 2')