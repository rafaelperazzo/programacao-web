# -*- coding: utf-8 -*-
n=int(input('digite n '))
primeiro=int(input('hora da entrada: '))
a=10
x=0
for i in range(1,n,1):
    b=int(input('hora da entrada: '))
    x=primeiro+a
    if primeiro-b>a:
        x=b+a+x
    else:
        x=x+a
    primeiro=b
    print(x)
