# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
import math
x=float(input("digite o valor de Xo:"))
for i in range (1,13,1):
    print(x)
    fx=(-x**3)-math.cos(x)
    dx=-(3*x**2)+math.sin(x)
    x=x-(fx)/(dx)
    
    
