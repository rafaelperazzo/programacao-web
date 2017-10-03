# -*- coding: utf-8 -*-
dia1=int(input("digite uma data: ")
mes1=int(input("digite um mês: ")
ano1=int(input("digite um ano: ")
dia2=int(input("digite outra data: ")
mes2=int(input("digite outro mês: ")
ano2=int(input("digite outro ano: ")

if ano1>ano2:
    print("DATA1")
elif ano2>ano1:
    print("DATA2")
else:
    if mes1>mes2:
        print("DATA1")
    elif mes2>mes1:
        print("DATA2")
    else:
        if dia1>dia2:
            print("DATA1")
        elif dia2>dia1:
            print("DATA2")
        else:
            print("IGUAIS")