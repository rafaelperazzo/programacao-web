# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO AQUI
t1=int(input("Tomadas da régua 1: "))
t2=int(input("Tomadas da régua 2: "))
t3=int(input("Tomadas da régua 3: "))
t4=int(input("Tomadas da régua 4: "))
while t1 <= 1 or t2 <= 1 or t3 <= 1 or t4 <= 1:
    print("Digite números inteiros maiores que 1")
    t1=int(input("Tomadas da régua 1: "))
    t2=int(input("Tomadas da régua 2: "))
    t3=int(input("Tomadas da régua 3: "))
    t4=int(input("Tomadas da régua 4: "))
tt=(t1-3)*(t2)*(t3)*(t4)
print(tt)