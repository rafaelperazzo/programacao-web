# -*- coding: utf-8 -*-
n=int(input('digite n: '))
a=[]
cont=0
for i in range (0,n,1):
    T=int(input('digite T: '))
    a.apend(T)
for i in range (1,len(a),1):
    soma=abs(a[i-1]-a[i])
    if soma>x9:
        x9=soma
print(x9)

