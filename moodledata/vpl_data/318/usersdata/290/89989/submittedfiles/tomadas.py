# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO AQUI
def n_tomadas(T1,T2,T3,T4):
    tom=((T1-1)+(T2-1)+(T3-1)+T4)
    return tom
a=int(input("Digite a: "))
while a<=1:
    a=int(input("Digite a: "))
b=int(input("Digite b: "))
while b<=1:
    b=int(input("Digite b: "))
c=int(input("Digite c: "))
while c<=1:
    c=int(input("Digite c: "))
d=int(input("Digite d: "))
while d<=1:
    d=int(input("Digite d: "))
print(n_tomadas(a,b,c,d))

