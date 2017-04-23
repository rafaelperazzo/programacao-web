#coding: utf-8
n=int(input('digite n: '))
a=1
for i in range(1,n+1,1):
    a=a+1
    b=a+b
    c=b+c
    d=c+d
    print(d)