# -*- coding: utf-8 -*-
n=int(input('digite n :'))
p=int(input('digite p :'))
cont=0
i=1
while i<=n:
    x=int(input('digite x :'))
    y=int(input('digite y :'))
    if (x+y)>=p:
        cont=cont+1
    else:
        cont=cont
        i=i+1
    print(cont)    