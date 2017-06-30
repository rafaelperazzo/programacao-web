# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('n: '))
a=[]
while n>=0:
    if n>=0:
        b=n%10
        a.append(b)
    else:
        a.append(n)
    n=n//10
    print(a)
