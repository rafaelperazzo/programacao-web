# -*- coding: utf-8 -*-
n=int(input('Digite o número em binário:'))
i=0
s=0
while n>0:
    m=n%10
    s=s+m*2**i
    n=n//10
    i=i+1
print(s)

