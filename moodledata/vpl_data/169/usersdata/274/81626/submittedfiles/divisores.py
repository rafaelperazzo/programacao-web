# -*- coding: utf-8 -*-
import math
n = int(input("Digite valor de multiplos: "))
a = int(input("Digite valor de a: "))
b = int(input("Digite valor de b: "))
c = 1
cont = 0
while (cont<n):
    if (c%a) == 0 or (c%b) ==0 :
        print(c)
        c = c+1
        cont = cont+1
    else:
        c = c+1 