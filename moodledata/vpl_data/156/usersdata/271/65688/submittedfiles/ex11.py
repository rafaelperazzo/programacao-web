# -*- coding: utf-8 -*-
#ENTRADA
dia1 = int(input('Digite o dia que nasceu: '))
mes1 = int(input('Digite o mes que nasceu: '))
ano1 = int(input('Digite o ano que nasceu: '))
dia2 = int(input('Digite o dia que nasceu: '))
mes2 = int(input('Digite o mes que nasceu: '))
ano2 = int(input('Digite o ano que nasceu: '))
DATA1 = ('dia1/mes1/ano1')
DATA2 = ('dia2/mes2/ano2')
IGUAIS = ('dia1/mes1/ano1') or ('dia2/mes2/ano2')

#PROCESSAMENTO
if ano1>ano2 :
    print(DATA2)
if ano1<ano2 :
    print(DATA1)
if ano1==ano2 and mes1>mes2 :
    print(DATA2)
if ano1==ano2 and mes1<mes2 :
    print(DATA1)
if ano1==ano2 and mes1==mes2 and dia1>dia2 :
    print(DATA2)
if ano1==ano2 and mes1==mes2 and dia1<dia2 :
    print(DATA1)
if ano1==ano2 and mes1==mes2 and dia1==dia2 :
    print(IGUAIS)

    

