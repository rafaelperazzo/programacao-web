# -*- coding: utf-8 -*-
p=int(input('digite o valor de p:'))
q=int(input('digite o valor de q:'))
contp=0
contq=0
for j in range (1,p+1,1):
    if p%j==0:
        contp=contp+1
for i in range (1,q+1,1):
    if q%i==0:
        contq=contq+1
if contp==2 and contq==2:
    if q==p+2:
        print('S')
else:
    print('N')
