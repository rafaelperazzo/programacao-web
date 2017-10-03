# -*- coding: utf-8 -*-
dia1 = int(input('digite o dia 1: '))
mes1 = int(input('digite o mes 1: '))
ano1 = int(input('digite o ano 1: '))
dia2 = int(input('digite o dia 2: '))
mes2 = int(input('digite o mes 2: '))
ano2 = int(input('digite o ano 2: '))
if ano1>ano2:
    print("data 1")
elif ano1<ano2:    
    print("data 1")
elif ano1==ano2 and mes2>mes1:
    print("data 2")
elif ano1==ano2 and mes2<mes1:
    print("data 1")
elif ano1==ano2 and mes2==mes1 and dia2>dia1:
    print("data 2")
elif ano1==ano2 and mes1==mes2 and dia2<dia1:
    print("data 1")
elif ano1==ano2 and mes1==mes2 and dia2==dia1:
    print("iguais")