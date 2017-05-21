# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
import math
a=3.14
b=4.5
for i in range(1,13,1):
    x=(a+b)/2
    y=(b-a)/2
    X=x/2+math.tan(math.radians(x))
    print(X)
    if A*X<0:
        b=x
    else:
        a=x