# -*- coding: utf-8 -*-
p=int(input('digite o valor de p:'))
q=int(input('digite o valor de q:'))
contq=0
contp=0
for j in range (1,p+1,1):
    if p%j==0:
        contp=contp+1
        if contp==2:
            b=p
for i in range (1,q+1,1):
    if q%i==0:
        contq=contq+1
        if contq==2:
            a=q
if a==b+2:
    print('S')
else:
    print('N')
