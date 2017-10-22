# -*- coding: utf-8 -*-
import math
T1=int(input("Digite T1: "))
while True:
    if T1<1:
        print("Valor inválido para T1")
        T1=int(input("Digite T1: "))
    else:
        break
T2=int(input("Digite T2: "))    
while True:   
    if T2<1:
        print("Valor inválido para T2")
        T2=int(input("Digite T2: "))
    else:
        break
T3=int(input("Digite T3: "))
while True:
    if T3<1:
        print("Valor inválido para T3")
        T3=int(input("Digite T3: "))
    else:
        break
T4=int(input("Digite T4: "))
while True:
    if T4<1:
        print("Valor inválido para T4")
        T4=int(input("Digite o valor de T4: "))
    else:
        break
disp=T1+T2+T3+T4-3
print(disp)