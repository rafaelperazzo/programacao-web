# -*- coding: utf-8 -*-
dia1 =int(input('digite o dia1'))
mes1 = int(input('digite o mes1'))
ano1 = int(input('digite o ano1'))
dia2 = int(input('digite o dia2'))
mes2 = int(input('digite o mes2'))
ano2 = int(input('digite o ano2'))
if (dia1==dia2) and (mes1==mes2) and (ano1==ano2):
    print("iguais")
elif (dia1<=dia2) and (mes1<=mes2) and (ano1<=ano2):
    print("data 1 menor")
else (dia1>=dia2) and (mes1>=mes2) and (ano1>=ano2):
    print("data 2 menor")
