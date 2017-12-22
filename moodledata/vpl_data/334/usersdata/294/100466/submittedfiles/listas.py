# -*- coding: utf-8 -*-
n= int(input('Digite o número de elementos: '))
while n<2:
    n= int(input('Digite o número de elementos: '))
a=[]
for i in range (0,n,1):
    a.append(int(input('Digite o elemento%d: ' %(i+1))))
for i in range (0,n-1,1):
    dif= a[i]-a[i+1]
    if dif>0:
        dif=dif*1
degrau=0
for i in range (0,n-1,1):
    if dif>degrau:
        degrau=dif
print(degrau)
