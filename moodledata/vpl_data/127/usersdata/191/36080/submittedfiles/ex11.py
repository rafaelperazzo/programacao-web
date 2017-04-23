# -*- coding: utf-8 -*-
dia1=int(input('digite o dia 1:'))
dia2=int(input('digite o dia 2:'))
mes1=int(input('digite o mes 1:'))
mes2=int(input('digite o mes 2:'))
ano1:int(input('digite o ano 1:'))
ano2:int(input('digite o ano 2:'))
if ano1>ano2:
    print('ano1')
elif ano2>ano1:
    print('ano2')
else:
    if mes1>mes2:
        print('mes1')
    elif mes2>mes1:
        print('mes2')
    else:
        if dia1>dia2:
            print('dia1')
        elif dia2>dia1:
            print('dia2')
        else:
            print('iguais')
    

