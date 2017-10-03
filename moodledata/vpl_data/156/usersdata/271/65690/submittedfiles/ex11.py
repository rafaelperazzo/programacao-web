# -*- coding: utf-8 -*-
#ENTRADA
dia1 = int(input('Digite o dia que nasceu: '))
mes1 = int(input('Digite o mes que nasceu: '))
ano1 = int(input('Digite o ano que nasceu: '))
dia2 = int(input('Digite o dia que nasceu: '))
mes2 = int(input('Digite o mes que nasceu: '))
ano2 = int(input('Digite o ano que nasceu: '))


#PROCESSAMENTO
if ano1>ano2 :
    print('DATA2')
if ano1<ano2 :
    print('DATA1')
if ano1==ano2 and mes1>mes2 :
    print('DATA2')
if ano1==ano2 and mes1<mes2 :
    print('DATA1')
if ano1==ano2 and mes1==mes2 and dia1>dia2 :
    print('DATA2')
if ano1==ano2 and mes1==mes2 and dia1<dia2 :
    print('DATA1')
if ano1==ano2 and mes1==mes2 and dia1==dia2 :
    print('IGUAIS')

    

