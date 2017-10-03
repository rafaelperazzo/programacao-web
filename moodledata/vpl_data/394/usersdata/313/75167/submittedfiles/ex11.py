# -*- coding: utf-8 -*-

dia1 = int(input('digite o valor em dia:'))
mes1 = int(input('digite o valor em mes:'))
ano1 = int(input('digite o valor em ano:'))
dia2 = int(input('digite o valor em dia:'))
mes2 = int(input('digite o valor em mes:'))
ano2 = int(input('digite o valor em ano:'))
if (dia1 == dia2) and (mes1 == mes2) and (ano1 == ano2):
    print ('IGUAIS')
elif (dia1 <= dia2) and (mes1 <= mes2) and (ano1 <= ano2):
    print('DATA 2')
else:
    print ('DATA 1')



