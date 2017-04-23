# -*- coding: utf-8 -*-
dia1=int(input('Digite Dia1: '))
mes1=int(input('Digite Mes1: '))
ano1=int(input('Digite Ano1: '))
dia2=int(input('Digite Dia2: '))
mes2=int(input('Digite Mes2: '))
ano2=int(input('Digite Ano2: '))
if ano1>ano2:
    print('DATA 1')
elif ano2>ano1:
    print('DATA 2')
else:
    if mes1>mes2:
        print('DATA 1')
    elif mes2>mes1:
        print('DATA 2')
    else:
        if dia1>dia2:
            print('DATA 1')
        elif dia2>dia1:
            print('DATA 2')
        else:
            print "DATAS IGUAIS"