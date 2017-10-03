# -*- coding: utf-8 -*-
dia1 = int(input("digite o dia 1:"))
med = int(input("digite o dia 1:"))
ano1 = int(input("digite o dia 1:"))
dia2 = int(input("digite o dia 2:"))
mes2 = int(input("digite o dia 2:"))
ano2 = int(input("digite o dia 2:"))
if dia1>dia2:
    if mes1>mes2: 
        if ano1>ano2:
            print(str("DATA1"))
if dia2>dia1:
    if mes2>mes1: 
        if ano2>ano1:
            print(str("DATA2"))
if dia1==dia2:
    if mes1==mes2: 
        if ano1==ano2:
            print(str("IGUAIS")) 
