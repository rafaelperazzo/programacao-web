# -*- coding: utf-8 -*-
dia1=int(input('digite o dia 1:'))
mes1=int(input('digite o mes 1:'))
ano1=int(input('digite o ano 1:'))

dia2=int(input('digite o dia 2:'))
mes2=int(input('digite o mes 2:'))
ano2=int(input('digite o ano 2:'))

if(ano1>ano2):
    print('data1')
elif(ano1<ano2):
    print('data2')
else:
    if(mes1>mes2):
        print('data1')
    elif(mes1<mes2):
        print('data2')
    else:
        if(dia1>dia2):
            print('data1')
        elif(dia1<dia2):
            print('data2')
        else:
            print('iguais')