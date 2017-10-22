# -*- coding: utf-8 -*-
import math

x1 = int(input("Digite o primeiro número: "))
x2 = int(input("Digite o segundo número: "))

i = 0

while (True):
    i +=1
    if i == x1 :
        break
    if x1 % i ==0 :
        i += x1

print(i)