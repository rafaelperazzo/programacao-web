# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=input(float("digite o limite a"))
b=input(float("digite o limite b"))
for i in range (1,10,1):
A=(3*(a+1)*(a-(1/2))*(a-1))
B= 3*(b+1)*(b-1/2)*(b-1)
x=(a+b)/2
fx= 3*(x+1)*(x-1/2)*(x-1)
    if A < 0 :
        b=x
    else:
        a=x
print(x)
print(a)
print(b)
        