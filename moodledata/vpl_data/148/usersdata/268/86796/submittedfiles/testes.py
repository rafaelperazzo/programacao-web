# -*- coding: utf-8 -*-

def impar(x):
    if x%2==1:
        return(True)
    else:
        return(False)
for i in range(1000,10000,1):
i1=i
a=i//10
i=i//10
b=i//10
i=i//10
c=i//10
i=i//10
d=i//10

if( a - b + c - d )<0:
    print(i1)
