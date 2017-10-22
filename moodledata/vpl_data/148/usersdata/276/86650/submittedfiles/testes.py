# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

dia1 = int(input('Digite o dia 1: '))
mes1 = int(input('Digite o mes 1: '))
ano1 = int(input('Digite o ano 1: '))
dia2 = int(input('Digite o dia 2: '))
mes2 = int(input('Digite o mes 2: '))
ano2 = int(input('Digite o ano 2: '))

if (ano1>ano2):
    print ('DATA1')
elif (ano2>ano1):
    print ('DATA2')
elif (ano1 == ano2) and (mes1>mes2):
    print ('DATA1')
elif (ano1 == ano2) and (mes2>mes1):
    print ('DATA2')
elif (ano1== ano2) and (mes1 == mes2) and (dia1> dia2):
    print ('DATA1')
elif (ano1== ano2) and (mes1 == mes2) and (dia2> dia1):
    print ('DATA2')
elif (ano1== ano2) and (mes1 == mes2) and (dia1 == dia2):
    print ('IGUAIS')
    aumento = investimento*taxadecrescimento
    investimento = investimento + aumento
    print(investimento)
    i = i + 1