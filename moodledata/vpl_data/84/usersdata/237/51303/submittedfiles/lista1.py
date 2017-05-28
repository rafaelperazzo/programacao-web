# -*- coding: utf-8 -*-
n=int(input("Digite n: "))
num=[]
for i in range(0,n,1):
    num.append(int(input("Digit em termo: ")))
    
s1=0
r2=0
s2=0
r2=0
for i in range(0,len(num),1):
    if num[i]%2!=0:
        s1=s1+1
        r1=r1+num[i]
    if num[i]%2==o:
        s2=s2+1
        r2=r2+1
print(r1)
print(r2)
print(s1)
print(s2)
print(num)
    
