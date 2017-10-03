# -*- coding: utf-8 -*-
import math
n = int(input("Digete n: "))
i = 1
while i<n:
    x = float(input("Digite x: "))
    y = float(input("digite y: "))
    if x>0 and y>0 and (x*x+x*y) <=1 :
        print("SIM")
    else:
        print("NAO")