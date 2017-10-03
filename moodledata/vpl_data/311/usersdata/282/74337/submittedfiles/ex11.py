# -*- coding: utf-8 -*-
dia1 = int(input('Digite o primeiro dia: '))
mes1 = int(input('Digite o primeiro mês: '))
ano1 = int(input('Digite o primeiro ano: '))
print('\n')
dia2 = int(input('Digite o segundo dia: '))
mes2 = int(input('Digite o segundo mes: '))
ano2 = int(input('Digite o segundo ano: '))
print('\n')
if ano1>ano2:   
    print('DATA 1')
elif ano1<ano2:
    print('DATA 2')
elif ano1 == ano2 and mes1>mes2:
    print('DATA 1')
elif ano1 == ano2 and mes1<mes2:
    print('DATA 2')
elif ano1 == ano2 and mes1 == mes2 and dia1>dia2:
    print('DATA 1')
elif ano1 == ano2 and mes1 == mes2 == dia1<dia2:
    print('DATA 2')
elif ano1 == ano2 and mes1 == mes2 == dia1 == dia2:
    print('IGUAIS')
           

