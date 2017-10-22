# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO AQUI
t1 = int(input("Digite o número de tomadas da régua 1: "))
while (t1<=1):
    t1 = int(input("Digite o número de tomadas da régua 1: "))
t2 = int(input("Digite o número de tomadas da régua 2: "))
while (t2<=1):
    t2 = int(input("Digite o número de tomadas da régua 2: "))
t3 = int(input("Digite o número de tomadas da régua 3: "))
while (t3<=1):
    t3 = int(input("Digite o número de tomadas da régua 3: "))
t4 = int(input("Digite o número de tomadas da régua 4: "))
while (t4<=1):
    t4 = int(input("Digite o número de tomadas da régua 4: "))
total = (t1-1)*(t2-1)*(t3-1)*t4
print(total)
