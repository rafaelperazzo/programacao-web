# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
import math
x=float(input("digite o valor de Xo:"))
for i in range (1,5,1):
    print(x)
    f=(-(x**3))- (math.cos(x))
    d=(-(3*x**2))+ (math.sin(x))
    x=x-((f)/(d))
    print(f)
    
