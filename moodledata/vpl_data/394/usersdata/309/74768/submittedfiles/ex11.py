# -*- coding: utf-8 -*-
dia1=int(input("Digite o dia da primeira data:"))
mes1=int(input("Digite o mês da primeira data:"))
ano1=int(input("Digite o ano da primeira data:"))

dia2=int(input("Digite o dia da segunda data:"))
mes2=int(input("Digite o mês da segunda data:"))
ano2=int(input("Digite o ano da segunda data:"))

if ano1>ano2:
    print("Data 1")
elif ano2>ano1 :
    print("Data2")
else :
    if mes1>mes2:
        print("Data1")
    elif mes2>mes1:
        print("data2")
    else:
        if dia1>dia2 :
            print("Data1")
        elif dia2>dia1 :
            print ("Data2")
        else:
            print("IGUAIS")