# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
import math
a=3
b=4.5
for i in range (1,13,1):
    x=(a+b)/2
    y=(b-a)/2
    A=((a/2)-(math.tan(a)))
    B=((b/2)-(math.tan(b)))
    X=((x/2)-(math.tan(x)))
    print(a)
    if A*X<0:
        b=x
    else:
        a=x
