# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
import math
x=float(input("digite o valor de Xo:"))
for i in range (1,10,1):
    f=(x**5)-(x**3)+3
    d=(4*x**4)-(3*x**2)
    x=x-((f)/(d))
    print(f)
    
    
