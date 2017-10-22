# -*- coding: utf-8 -*-
n=int(input(''))
t=0
t1=0
for i in range(n):
    if t1-t<10:
        t1=int(input(''))
    else:
        t=t1+10
print(t1)

    