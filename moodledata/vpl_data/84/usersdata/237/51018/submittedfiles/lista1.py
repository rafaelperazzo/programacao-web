# -*- coding: utf-8 -*-
n=int(input("Digite n: "))
num=[]
a=1
i=0
s1=0
s2=0
q=0
t=0
while a<=n:
    num.append(input("Digite: "))
    a=a+1
while i<n:
    r=num[i]
    if r%2==0:
        s1=s1+r
        q=q+1
    elif r%2!=0:
        s2=s2+r
        t=t+1
print(s2)
print(s1)
print(t)
print(q)
print(num)

