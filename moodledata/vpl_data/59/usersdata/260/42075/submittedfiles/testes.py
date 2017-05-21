# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=float(input("digite o limite a:"))
b=float(input("digite o limite b:"))
for i in range (1,3,1):
    A=(3*(a+1)*(a-(1/2))*(a-1))
    B= 3*(b+1)*(b-1/2)*(b-1)
    x=(a+b)/2
    X= 3*(x+1)*(x-1/2)*(x-1)
    print("o valor de a será"a)
    print(b)
    print(x)
    if (A*X<0):
        b=x
    else:
        a=x
    