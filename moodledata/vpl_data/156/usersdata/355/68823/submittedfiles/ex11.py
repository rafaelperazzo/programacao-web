# -*- coding: utf-8 -*-
print('Data nº1')
dia1= float(input('dia: '))
mes1= float(input('mês: '))
ano1= float(input('ano: '))
print('Data nº2')
dia2= float(input('dia: '))
mes2= float(input('mês: '))
ano2= float(input('ano: '))

if (ano1>ano2):
    print('DATA 1')
else:
    print('DATA 2')
elif (ano1==ano2) and (mes1>mes2):
    print('DATA 1')
else:
    print('DATA 2')
if (ano1==ano2) and (mes1==mes2) and (dia1>dia2):
    print('DATA 1')
else:
    print('DATA 2')
if (ano1==ano2) and (mes1==mes2) and (dia1==dia2):
    print('IGUAIS')