# -*- coding: utf-8 -*-

dia1= int(input('Digite um dia:'))
mes1= int(input('Digite um mês:'))
ano1= int(input('Digite um ano:'))
dia2= int(input('Digite um dia:'))
mes2= int(input('Digite um mês:'))
ano2= int(input('Digite um ano:'))

if ano1>ano2:
    print('DATA 1')
elif ano1<ano2:
    print('DATA 2')
else:
    if mes1>mes2:
        print('DATA 1')
    elif mes1<mes2:
        print('DATA 2')
    else:
        if dia1>dia2:
            print('DATA 1')
        elif dia1<dia2:
            print('DATA 2')
        else:
            print('IGUAIS')