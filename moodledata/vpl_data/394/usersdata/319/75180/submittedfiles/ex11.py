# -*- coding: utf-8 -*-
dia1=int(input('digite dia1: '))
mes1=int(input('digite mes1: '))
ano1=int(input('digite ano1: '))
dia2=int(input('digite dia2: '))
mes2=int(input('digite mes2: '))
ano2=int(input('digite ano2: '))

if ano1==ano2:
    if mes1==mes2:
        if dia1==dia2:
            print('IGUAIS')
        elif dia2>dia1:
            print('DATA 2')
        else:
            print('DATA 1')
    elif mes2>mes1:
        print('DATA 2')
    elif mes1>mes2:
        print('DATA 1')
elif ano2>ano1:
    print('DATA 2')
else:
    print('DATA 1')

