# -*- coding: utf-8 -*-
d1=int(input("Digite o Dia1: "))
m1=int(input("Digite o Mês1: "))
a1=int(input("Digite o Ano1: "))
d2=int(input("Digite o Dia2: "))
m2=int(input("Digite o Mês2: "))
a2=int(input("Digite o Ano2: "))

if a1>a2:
    print("DATA 1")
elif a2>a1:
    print("DATA 2")
else:
    if m1>m2:
        print("DATA 1")
    elif m2>m1:
        print("DATA 2")
    else:
        if d1>d2:
            print("DATA 1")
        elif d2>d1:
            print("DATA 2")
        else:
            print("DATAS IGUAIS")