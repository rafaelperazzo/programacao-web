# -*- coding: utf-8 -*-
q=int(input('digite o valor de q:'))
p=int(input('digite o valor de p:'))
contq=0
contp=0
for i in range (1,q+1,1):
    if q%i==0:
        contq=contq+1
        if contq==2:
            q=q
for j in range (1,p+1,1):
    if p%j==0:
        contp=contp+1
        if contp==2:
            p=p
if q==p+2:
    print('S')
else:
    print('N')
