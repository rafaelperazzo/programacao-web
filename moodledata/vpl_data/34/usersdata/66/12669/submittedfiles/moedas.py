# -*- coding: utf-8 -*-
from __future__ import division
a=int(input("digite a:"))
b=int(input("digite b:"))
c=int(input("digite c:"))
if c%2==1 and a%2==0 and b%2==0:
    prin ("N")
elif c%2==0 and a%2==1 and b%2==1:
    prin ("N")
x=1
y=1
while a*x + b*y==c:
    x=x+1
    y=y+1
    
print x
print y