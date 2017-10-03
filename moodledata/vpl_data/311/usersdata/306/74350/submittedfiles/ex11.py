# -*- coding: utf-8 -*-
a=int(input("Digite o dia X: "))
b=int(input("Digite o mês X: "))
c=int(input("Digite o ano X: "))
e=int(input("Digite o dia Y: "))
f=int(input("Digite o mês Y: "))
g=int(input("Digite o ano Y: "))

DATA1=(c*100000)+(b*1000)+(a*100)
DATA2=(e*100000)+(f*1000)+(g*100)

if DATA1>DATA2:
    print("DATA1")
else:
    print("DATA2")

