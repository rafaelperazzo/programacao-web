# -*- coding: utf-8 -*-
c=[]
n=int(input("Digite n: "))
for i in range (0,n,1):
    c.append(int(input("Digite o termo: ")))
a=0
for i in range(1,len(c),1):
    o=a[i]-a[i-1]
    if o<0:
        o=o*(-1)
    else:
        o=o+0
    if o>a:
        a=o+a
    else:
        a=a+0
print(a)

