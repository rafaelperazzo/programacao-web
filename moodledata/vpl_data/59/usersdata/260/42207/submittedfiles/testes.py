# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
import math
x=float(input("digite o valor de Xo:"))
for i in range (1,5,1):
    f=math.exp(x)-3*x**2
    d=math.exp(x)-6*x
    x=x-((f)/(d))
    print(x)
    
