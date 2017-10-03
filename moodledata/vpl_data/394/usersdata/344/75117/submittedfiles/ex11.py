# -*- coding: utf-8 -*-

dia1 = int(input("digite o dia 1: "))
mes1 = int(input("digite o mes 1: "))
ano1 = int(input("digite o ano 1: "))
dia2 = int(input("digite o dia 2: "))
mes2 = int(input("digite o mes 2: "))
ano2 = int(input("digite o ano 2: "))

if (dia1 == dia2) and (mes1 == mes2) and (ano1 == ano2):
    print ('IGUAIS')
elif (dia1 <= dia2) and (mes1 <= mes2) and (ano1 <= ano2):
    print ('DATA 2')
else:
    print ('DATA 1')