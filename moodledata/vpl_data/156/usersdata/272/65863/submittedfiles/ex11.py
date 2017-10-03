# -*- coding: utf-8 -*-

dia1= int(input('Digite o dia:'))
mes1= int(input('Digite o mês:'))
ano1= int(input('Digite o ano:'))

dia2= int(input('Digite o dia:'))
mes2= int(input('Digite o mês:'))
ano2= int(input('Digite o ano:'))

if (dia1>dia2) and (mes1>mes2) and (ano1>ano2):
    print('DATA 1')


elif (dia1>dia2) and (mes1==mes2) and (ano1==ano2):
    print('DATA 1')
    
elif (dia1==dia2) and (mes1>mes2) and (ano1==ano2):
    print('DATA 1')

elif (dia1==dia2) and (mes1==mes2) and (ano1>ano2):
    print('DATA 1')

elif (dia1>dia2) and (mes1>mes2) and (ano1==ano2):
    print('DATA 1')

elif (dia1==dia2) and (mes1>mes2) and (ano1>ano2):
    print('DATA 1')

elif (dia1<dia2) and (mes1<mes2) and (ano1<ano2):
    print('DATA 2')

elif (dia1<dia2) and (mes1==mes2) and (ano1==ano2):
    print('DATA 2')
    
elif (dia1==dia2) and (mes1<mes2) and (ano1==ano2):
    print('DATA 2')

elif (dia1==dia2) and (mes1==mes2) and (ano1<ano2):
    print('DATA 2')

elif (dia1<dia2) and (mes1<mes2) and (ano1==ano2):
    print('DATA 2')

elif (dia1==dia2) and (mes1<mes2) and (ano1<ano2):
    print('DATA 2')

elif (dia1==dia2) and (mes1==mes2) and (ano1==ano2):
    print('IGUAIS')
