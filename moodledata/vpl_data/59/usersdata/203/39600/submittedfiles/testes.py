#coding: utf-8
n=int(input('digite n: '))
s=1/n
for i in range(1,n,1):
    s=s+(i/(n-i))
print(s)