# -*- coding: utf-8 -*-
dia1=float(input(""))
mes1=float(input(""))
ano1=float(input(""))
dia2=float(input(""))
mes2=float(input(""))
ano2=float(input(""))
if ano1>ano2:
    print("DATA 1")
elif ano1==ano2:
    if mes1>mes2:
        print("DATA 1")
    elif mes1==mes2:
        if dia1>dia2:
            print("DATA 1")
        elif dia1==dia2:
            print("IGUAIS")
        else:
            print("DATA 2")
    else:
        print("DATA 2")
else:
    print("DATA 2")
