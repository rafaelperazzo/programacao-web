# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

dia1 = int(inpu('Digite o dia 1 '))
mes1 = int(inpu('Digite o mes 1 '))
ano1 = int(inpu('Digite o ano 1 '))
dia2 = int(inpu('Digite o dia 2 '))
mes2 = int(inpu('Digite o mes 2 '))
ano2 = int(inpu('Digite o ano 2 '))

if dia1 == dia2 and mes1 == mes2 and ano1 == ano2:
    print ('iguais')
if ano1 > ano2:
    print ('data 1')
else:
    print ('data 2')
if ano1 == ano2 and mes1 > mes2:
    print('data 1')
else:
    print ('data 2')
if ano1 == ano2 and mes1 == mes2 and dia1 > dia2:
    print ('data 1')
else:
    print ('data 2')