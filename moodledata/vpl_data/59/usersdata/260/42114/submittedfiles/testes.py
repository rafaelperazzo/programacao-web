# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
import math
a=3
b=5
for i in range (1,20,1):
    x=(a+b)/2
    y=(b-a)/2
    A= a/2+math.tan(a)
    B=a/2+math.tan(a)
    X=a/2+math.tan(a)
    print(x)
    if (A*X<0):
        b=x
    else:
        a=x
    