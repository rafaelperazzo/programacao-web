# -*- coding: utf-8 -*-
def diferença(x,y):
    d=x-y
    if d<0:
        d=d*(-1)
        return d
    else:
        return d
a=[]
n=int(input("Digite a quantidade de elemtos da lista, sendo >=2: "))
while n<2:
    n=int(input("Digite a quantidade de elemtos da lista, sendo >=2: "))
for i in range(0,n,1):
    a.append(int(input("Digite um valor para sua sequência: ")))
c=0
for i in range(0,n,1):
    if diferença(a[i],a[i+1])>c:
        c=diferença(a[i],a[i+1])
print(c)
    
