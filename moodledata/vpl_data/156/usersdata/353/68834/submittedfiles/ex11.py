# -*- coding: utf-8 -*-
#ENTRADA
dia1 = int(input('Dia 1: '))
mes1 = int(input('Mes 1: '))
ano1 = int(input('Ano 1: '))
dia2 = int(input('Dia 2: '))
mes2 = int(input('Mes 2: '))
ano2 = int(input('Ano 2: '))
#PROCESSAMENTO
if ano1>ano2:
    print ('DATA 1')
elif ano2>ano1:
    print ('DATA 2')
else:
    if mes1>mes2:
        print ('DATA 1')
    elif mes2>mes1:
        print ('DATA 2')
    else:
        if dia1>dia2:
            print ('DATA 1')
        elif dia2>dia1:
            print ('DATA 2')
        else:
            print ('IGUAIS')
        
