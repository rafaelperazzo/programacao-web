# -*- coding: utf-8 -*-
dia1 = int(input("Digite um dia: "))
mes1 = int(input("Digite um mês: "))
ano1 = int(input("Digite um ano: "))
print("\n")
dia2 = int(input("Digite um dia: "))
mes2 = int(input("Digite um mês: "))
ano2 = int(input("Digite um ano: "))
data1 = d1/m1/a1
data2 = d2/m2/a2
if ano1>ano2:
    print("DATA 1")
if ano1<ano2:
    print("DATA 2")
if ano1==ano2:
    if mes1>mes2:
        print("DATA 1")
    if mes1<mes2:
        print("DATA 2")
    if mes1==mes2:
        if dia1>dia2:
            print("DATA 1")
        if dia1<dia2:
            print("DATA 2")
        if dia1==dia2:
            print("IGUAIS")
