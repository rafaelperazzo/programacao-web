# -*- coding: utf-8 -*-
n=int(input('digite quantas pessoas detectadas :'))
i=0
for i in range(1,n+1,1):
    s=int(input('digite o instante  :'))
    if (i==1):
        s1=s
    elif (i==n):
        s2=s
tempo=s2-s1+10
print(tempo)
