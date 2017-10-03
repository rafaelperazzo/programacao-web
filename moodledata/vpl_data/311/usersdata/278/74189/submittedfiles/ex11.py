# -*- coding: utf-8 -*-
d1 = int(input("Digite um dia: "))
m1 = int(input("Digite um mês: "))
a1 = int(input("Digite um ano: "))
print("\n")
d2 = int(input("Digite um dia: "))
m2 = int(input("Digite um mês: "))
a2 = int(input("Digite um ano: "))
data1 = d1/m1/a1
data2 = d2/m2/a2
if a1>a2:
    print("DATA 1")
if a1<a2:
    print("DATA 2")
if a1==a2:
    if m1>m2:
        print("DATA 1")
    if m1<m2:
        print("DATA 2")
    if m1==m2:
        if d1>d2:
            print("DATA 1")
        if d1<d2:
            print("DATA 2")
        if d1==d2:
            print("IGUAIS")
