# -*- coding: utf-8 -*-
n=int(input('digite n:'))
i=0
s=0
while n//10!=0:
    resto=n%10
    s=s+resto*2**i
    i=i+1
    print('%d'%s)

