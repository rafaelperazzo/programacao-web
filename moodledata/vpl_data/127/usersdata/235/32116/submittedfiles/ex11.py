# -*- coding: utf-8 -*-
dia1=int(input('digite o 1º dia:'))
mes1=int(input('digite o 1º mes:'))
ano1=int(input('digite o 1º ano:'))
dia2=int(input('digite o 2º dia:'))
mes2=int(input('digite o 2º mes:'))
ano2=int(input('digite o 2º ano:'))
if ano1>ano2:
    print('data 1')
elif ano1<ano2:
    print('data 2')
elif ano1==ano2 and mes1>mes2:
    print('data 1')
elif ano1==ano2 and mes1<mes2:
    print('data 2')