# -*- coding: utf-8 -*-
q=int(input('digite o valor de q:'))
p=int(input('digite o valor de p:'))
contq=0
contp=0
for i in range (1,q+1,1):
    if q%i==0:
        contq=contq+1
for i in range (1,p+1,1):
    if p%i==0:
        contp=contp+1
