# -*- coding: utf-8 -*-
a=[]
n=int(input("Digite a quantidade de elemtos da lista, sendo >=2: "))
while n<2:
    n=int(input("Digite a quantidade de elemtos da lista, sendo >=2: "))
for i in range(0,n,1):
    a.append(int(input("Digite um valor para sua sequência: ")))
c=0
d=0
print(a[0]-a[1])
for i in range(0,n,1):
    if a[i]>=a[i+1]:
        if a[i]-a[i+1]>c:
            c=a[i]-a[i+1]
    else:
        (a[i]-a[i+1])*(-1)
        if a[i]-a[i+1]>d:
            d=a[i]-a[i+1]
if c>=d:
    print(c)
else:
    print(d)
    
