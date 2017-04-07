# -*- coding: utf-8 -*-
dia1=int(input('digite o dia da data1:'))
mes1=int(input('digite o mes da data1:'))
ano1=int(input('digite o ano da data1:'))
dia2=int(input('digite o dia da data2:'))
mes2=int(input('digite o mes da data2:'))
ano2=int(input('digite o ano da data2:'))
if (ano1>ano2):
    print('DATA1')
elif (ano2>ano1):
    print('DATA2')
else :
    if mes1>mes2:
        print('DATA1')
    elif mes2>mes1:
        print('DATA2')
    else :
        if dias1>dias2:
            print('DATA1')
        elif dias2>dias1:
            print('DATA2')
        else :
            print('IGUAIS')
            
            
            
            
    