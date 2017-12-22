# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO AQUI
T1=int(input("Digite T1: "))
while T1<=1:
    T1=int(input("Digite T1: "))
T2=int(input("Digite T2: "))
while T2<=1:
    T2=int(input("Digite T2: "))
T3=int(input("Digite T3: "))
while T3<=1:
    T3=int(input("Digite T3: "))
T4=int(input("Digite T4: "))
while T4<=1:
    T4=int(input("Digite T4: "))
def n_tomadas(T1,T2,T3,T4):
    tom=((T1-1)+(T2-1)+(T3-1)+T4)
    return tom
print(tom)

