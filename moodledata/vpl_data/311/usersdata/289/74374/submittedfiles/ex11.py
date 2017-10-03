# -*- coding: utf-8 -*-
dia1 = int(input('Digite o dia 1: '))
mes1 = int(input('Digite o mes 1: '))
ano1 = int(input('Digite o ano 1: '))
dia2 = int(input('Digite o dia 2: '))
mes2 = int(input('Digite o mes 2: '))
ano2 = int(input('Digite o ano 2: '))
if ano1>ano2:
    print('DATA 1')
if ano1<ano2:
    print('DATA 2')
if ano1==ano2:
    if mes1>mes2:
        print('DATA 1')
    if mes1<mes2:
        print('DATA 2')
    if mes1==mes2:
        if dia1>dia2:
            print('DATA 1')
        if dia1<dia2:
            print('DATA 2')
        if dia1==dia2:
            print('IGUAIS')
            

