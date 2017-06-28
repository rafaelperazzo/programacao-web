# -*- coding: utf-8 -*-

def maior(a):
    for i in range(0,len(a)-1,1):
        g=a[i+1]-a[i]
            return(g)
        
n=int(input('digite o total de números:'))
x=[]

for i in range(0,n,1):
    d=int(input('digite os elementos:'))
    x.append(d)
print(maior(x))

