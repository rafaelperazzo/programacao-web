# -*- coding: utf-8 -*-
dia1 = int(input("Dgite o dia 1: "))
mes1 = int(input("Digite o mês 1: "))
ano1 = int(input("Digite o ano 1: "))
dia2 = int(input("Dgite o dia 2: "))
mes2 = int(input("Digite o mês 2: "))
ano2 = int(input("Digite o ano 2: "))
if dia1>dia2:
    if mes1>mes2:
        if ano1>ano2:
            print (str("DATA 1"))
if dia1<dia2:
    if mes1<mes2:
        if ano1<ano2:
            print(str("DATA 2"))
if dia1!= dia2:
    if mes1!= mes2:
        if ano1 != ano2:
                print(str("IGUAIS"))
            