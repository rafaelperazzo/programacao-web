# -*- coding: utf-8 -*-
dia1 = int(input("dia1? :"))
mes1 = int(input("mes1? :"))
ano1 = int(input("ano1? :"))
dia2 = int(input("dia2? :"))
mes2 = int(input("mes2? :")) 
ano2 = int(input("ano2? :"))

if ano1 == ano2 and mes1 == mes2 and dia1 == dia2 :
    print("IGUAIS")
elif:
    if ano1 > ano2 :
        if mes1 > mes2 :
            if dia1 > dia2 :
                print("DATA 1")
    else: 
        if ano1 < ano2 :
            if mes1 < mes2 :
                if dia1 < dia2 :
                    print("DATA 2")