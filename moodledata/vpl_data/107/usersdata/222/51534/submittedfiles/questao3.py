# -*- coding: utf-8 -*-
a=int(input('a:'))
b=int(input('b:'))
cont=0
i=2
while i<a and i<b:
    if a%i==0 and b%i==0:
        cont=cont+1
    i=i+1