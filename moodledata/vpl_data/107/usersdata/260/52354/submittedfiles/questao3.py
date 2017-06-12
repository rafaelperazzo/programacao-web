# -*- coding: utf-8 -*-
p=int(input("digite o valor de p: "))
q=int(input("digite o valor de q: "))
dp=0
dq=0
for i in range(1,q*p,1):
    if q%i==0:
        dq=dq+1
    if p%i==0:
        dp=dp+1
if dp==2 and dq==2 and q==p+2 :
    print("S")
else:
    print("N")
