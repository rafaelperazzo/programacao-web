# -*- coding: utf-8 -*-
dia1 =int(input('digite o dia1'))
mes1 = int(input('digite o mes1'))
ano1 = int(input('digite o ano1'))
dia2 = int(input('digite o dia2'))
mes2 = int(input('digite o mes2'))
ano2 = int(input('digite o ano2'))
data1 = dia1 == mes1 == ano1
data2 = dia2 == mes2 == ano2
if data1>data2:
    print("data2 menor")
elif data1<data2:
    print("data1 menor")
else:
    print("iqual")
