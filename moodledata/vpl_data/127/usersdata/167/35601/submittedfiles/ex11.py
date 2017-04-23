# -*- coding: utf-8 -*-
dia1=int(input('digite dia 1:'))
dia2=int(input('digite dia 2:'))
mes1=int(input('digite mes 1:'))
mes2=int(input('digite mes 2:'))
ano1=int(input('digite ano 1:'))
ano2=int(input('digite ano 2:'))
if ano1>ano2:
    print('DATA 1')
else:
    if mes1>mes2:
        print('DATA 1')
    else:
        if dia1>dia2:
            print('DATA 1')
        elif dia2>dia1:
            print('DATA 2')
        else:
            ('iguais')
    
    