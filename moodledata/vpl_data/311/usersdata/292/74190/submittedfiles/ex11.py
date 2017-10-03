# -*- coding: utf-8 -*-
dia1=str(input("Digite o dia da DATA 1: "))
mes1=str(input("Digite o mês da DATA 1: "))
ano1=str(input("Digite o ano da DATA 1: "))
dia2=str(input("Digite o dia da DATA 2: "))
mes2=str(input("Digite o mês da DATA 2: "))
ano2=str(input("Digite o ano da DATA 2: "))
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
