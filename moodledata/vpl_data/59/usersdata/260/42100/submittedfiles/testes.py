# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=-2
b=1.25
for i in range (1,5,1):
    x=(a+b)/2
    y=(b-a)/2
    A=3*(a+1)*(a-1/2)*(a-1)
    B=3*(b+1)*(b-1/2)*(b-1)
    X=3*(x+1)*(x-1/2)*(x-1)
    print(y)
    if (A*X<0):
        b=x
    else:
        a=x
    