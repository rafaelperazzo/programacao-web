# -*- coding: utf-8 -*-
import math
n=int(input("Digite o valor de n: "))
a=int(input("Digite o valor de a: "))
b=int(input("Digite o valor de b: "))
p=1
c=a
d=b
for i in range(1,n+1,1):
    if a<b and a*i!=b*i:
        c=c*i
        d=d*i
        print(c)
        print(d)
    if b<a and a*i!=b*i:
        d=d*i
        c=c*i
        print(d)
        print(c)
    if a==b:
        c=c*i
        print(c)
    if a<b and a*i==b*i:
        c=c*i
        print(c)
    if b<a and a*i==b*i:
        d=d*i
        print(d)
        
        
    
    
