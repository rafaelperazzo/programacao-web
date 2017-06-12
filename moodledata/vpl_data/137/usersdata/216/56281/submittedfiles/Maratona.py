# -*- coding: utf-8 -*-
n=int(input('Digite n:'))
p=int(input('Digite p:'))
a=[]
i=0

for i in range(1,n+1,1):
    r= int(input('Digite r:'))
    i=i+1
    a.append(r)
for i in range(1,len(a)-1,1):
    if (a[i+1]-a[i])<p:
        print('s')
    else:
        print('n')