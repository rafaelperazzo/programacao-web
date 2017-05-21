# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
import math
a=3.14
b=4.5
for i in range(1,13,1):
    x=(a+b)/2
    y=(b-a)/2
    X=x/2+math.tan(math.pi(x))
    A=a/2+math.tan(math.pi(a))
    B=b/2+math.tan(math.pi(b))
    print(a)
    if A*X<0:
        b=x
    else:
        a=x