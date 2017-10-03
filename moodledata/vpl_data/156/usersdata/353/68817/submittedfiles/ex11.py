# -*- coding: utf-8 -*-
#ENTRADA
dia1 = int(input('Dia 1: '))
mes1 = int(input('Mes 1: '))
ano1 = int(input('Ano 1: '))
dia2 = int(input('Dia 2: '))
mes2 = int(input('Mes 2: '))
ano2 = int(input('Ano 2: '))
#PROCESSAMENTO
if dia1==dia2 and mes1==mes2 and ano1==ano2:
    print ('IGUAIS')
if dia1==dia2 and mes1==mes2 and ano1>ano2:
    print (ano1)
