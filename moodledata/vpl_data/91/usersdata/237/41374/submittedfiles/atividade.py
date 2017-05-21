# -*- coding: utf-8 -*-
n=int(input("Digite n: "))
x=1
c=1
while x<n:
    if n%x >0:
        c=c+1
    x=x*10
        
print(c)