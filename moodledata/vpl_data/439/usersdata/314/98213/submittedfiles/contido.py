# -*- coding: utf-8 -*-
def interseccao(a,b):
    cont=0
    for j in range(0,len(a)-1,1):
        for i in range(j+1,len(a)-1,1):
            if str(a[i]) in str(b[i]):
                cont+=1
    print(cont)
    return interseccao     



n=int(input('Digite n: '))
m=int(input('Digite m: '))
a=[]
b=[]
for i in range(0,n,1):
    a.append(int(input('Digite elementos de a: ')))
for i in range(0,m,1):
    b.append(int(input('Digite ementos de b: ')))

interseccao(a,b)

    