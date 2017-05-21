# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=float(input('digite n:'))
s=0
for i in range(1,n+2,1):
    if i%2==1:
        s=s+1/i
    else:
        s=i
print(s)
        
    