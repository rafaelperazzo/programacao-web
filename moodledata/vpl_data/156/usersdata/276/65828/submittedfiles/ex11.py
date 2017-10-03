# -*- coding: utf-8 -*-
dia1 = int(input('Digite o dia da primeira data: '))
mes1 = int(input('Digite o mes da primeira data: '))
ano1 = int(input('Digite o ano da primeira data: '))

dia2 = int(input('Digite o dia da segunda data: '))
mes2 = int(input('Digite o mes da segunda data: '))
ano2 = int(input('Digite o ano da segunda data: '))

if (ano2>ano1):
    print ('DATA 2')
elif (ano1>ano2):
    print ('DATA 1')
elif (ano1==ano2):
    if (mes2>mes1):
        print ('DATA 2')
    elif (mes1>mes2):
        print ('DATA 1')
    elif (mes1==mes2):
        if (dia2>dia1):
            print ('DATA 2')
        elif (dia1>dia2):
            print ('DATA 1')
        elif (dia1==dia2):
            print ('IGUAIS')
        