# -*- coding: utf-8 -*-
dia1=int(input("digite o dia da primeira data: "))
mes1=int(input("digite o mes da primeira data: "))
ano1=int(input("digite o ano da primeira data: "))
dia2=int(input("digite o dia da segunda data: "))
mes2=int(input("digite o mes da segunda data: "))
ano2=int(input("digite o ano da segunda data: "))
if (dia1==dia2) and (mes1==mes2) and (ano1==ano2):
    print("IGUAIS")
elif (ano1>ano2):
    print("DATA 1")
elif(ano1<ano2):
    print("DATA 2")
elif (ano1==ano2):
    if (mes1>mes):
        print("DATA 1")
    elif(mes1<mes2):
        print("DATA 2"):
    elif (mes1==mes2):
        if(dia1>dia2):
            print("DATA 1")
        elif(dia1<dia2):
            print("DATA 2")