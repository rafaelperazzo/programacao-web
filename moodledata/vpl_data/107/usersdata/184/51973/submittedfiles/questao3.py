# -*- coding: utf-8 -*-
p=int(input('digite p:'))
q=int(input('digite q:'))
contp=0
contq=0
for i in range(2,p,1):
    if p%i==0:
        contp=contp+1
for i in range(2,q,1):
    if q%i==0:
        contq=contq+1
if contp==0 and contq==0:
    a=p+2
    if q==a:
        print('S')
    else:
        print('N')