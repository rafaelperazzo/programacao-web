# -*- coding: utf-8 -*-

Dia1 = input('Digite dia1: ')
Mes1 = input('Digite mês1: ')
Ano1 = input('Digite ano1: ')

Dia2 = input('Digite dia2: ')
Mes2 = input('Digite mês2: ')
Ano2 = input('Digite ano2: ')

if Ano1 == Ano2 and Mes1 == Mes2 and Dia1 == Dia2:
    print('IGUAIS')

else:
    if Ano1 > Ano2:
        print('DATA1')
    if Ano1 < Ano2:
        print('DATA2')
    if Ano1 == Ano2:
        if Mes1 > Mes2:
            print('DATA1')
        if Mes1 < Mes2:
            print('DATA2')
        else:
            if Dia1 > Dia2:
                print('DATA1')
            if Dia1 < Dia2:
                print('DATA2')


    
    
    