# -*- coding: utf-8 -*-
n=int(input(''))
cont=0
t=0
for i in range(n):
    t1=int(input(''))
    if t1-t<10:
        t=int(input(''))
        cont=cont+t
print(cont)
    
    