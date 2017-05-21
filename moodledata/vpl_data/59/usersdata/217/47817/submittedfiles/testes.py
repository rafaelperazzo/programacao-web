# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=input('digite n:')
s=1
for i in range(1,n+2,1):
    if i%2==1:
        s=i
    else:
        s=s+1/i
print(s)
        
    