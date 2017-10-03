# -*- coding: utf-8 -*-
a=int(input("Digite o dia X: "))
b=int(input("Digite o mês X: "))
c=int(input("Digite o ano X: "))
d=int(input("Digite o dia Y: "))
e=int(input("Digite o mês Y: "))
f=int(input("Digite o ano Y: "))

DATA1=(c*100000)+(b*1000)+(a*100)
DATA2=(f*100000)+(e*1000)+(d*100)

if DATA1>DATA2:
    print("DATA1")
elif DATA1<DATA2:
    print("DATA2")
elif DATA1==DATA2:
    print("IGUAIS")

