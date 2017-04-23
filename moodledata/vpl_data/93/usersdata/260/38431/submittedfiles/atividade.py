# -*- coding: utf-8 -*-
import math
n=int(input("digite o valor de n"))
for i in range (1,n+1,1):
    x=float(input("digite os valores de x:"))
    y=float(input("digite os valores de y:"))
    if (((x>=0) and (y>=0)) and (x**2 + y**2 <=1)):
        print("sim")
    else:
        print("nao")