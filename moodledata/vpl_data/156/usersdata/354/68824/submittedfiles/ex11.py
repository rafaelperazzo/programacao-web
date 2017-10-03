# -*- coding: utf-8 -*-
dia1=int(input('Digite o valor do dia1: '))
mes1=int(input('Digite o valor do mes1: '))
ano1=int(input('Digite o valor do ano1: '))
dia2=int(input('Digite o valor do dia2: '))
mes2=int(input('Digite o valor do mes2: '))
ano2=int(input('Digite o valor do ano2: '))
#PROCESSAMENTO
if ano1>ano2:
    print ('DATA 1')
elif ano1<ano2:
    print('DATA 2')
else ano1==ano2:
    if mes1>mes2:
        print('DATA 1')
    elif mes1<mes2:
        print('DATA 2')
    else mes1==mes2:
        if dia1>dia2:
            print('DATA 1')
        elif dia1<dia2:
            print('DATA 2')
        else dia1=dia2:
            print('IGUAIS')

