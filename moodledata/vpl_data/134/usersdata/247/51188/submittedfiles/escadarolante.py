# -*- coding: utf-8 -*-
n=int(input('digite n '))
primeiro=int(input('hora da entrada: '))
a=10
x=0
h=primeiro
for i in range(1,n,1):
    b=int(input('hora da entrada: '))
    if h-b>-a:
        x=b+a-primeiro
    else:
        x=x+a
    x=h+a
    h=b
    print(x)
