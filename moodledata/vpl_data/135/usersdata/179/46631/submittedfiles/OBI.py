# -*- coding: utf-8 -*-
n=int(input('digite n :'))
p=int(input('digite p :'))
cont=0
while n>0:
    x=int(input('digite x :'))
    y=int(input('digite y :'))
    if (x+y)>=p:
        cont=cont+1
    else cont=cont    
        n=n-1
print(cont)    