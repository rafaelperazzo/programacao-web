# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('digite n:'))
s=1
for i in range(1,n+1,1):
    if i%2==1:
        s=s+1/i
    else:
        s=1/i
print(s)
        
    