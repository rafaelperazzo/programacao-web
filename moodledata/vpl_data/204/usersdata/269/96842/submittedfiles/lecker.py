# -*- coding: utf-8 -*-
def lecker(a):
    cont=0
    if a[0]>a[1]:
        cont=cont+1
    for i in range(1,len(a)-1,1):
        if a[i-1]<a[i] and a[i]>a[i+1]:
            cont=cont+1
    if a[len(a)-1]>a[len(a)-2]:
        cont=cont+1
    if cont==1:
        return(TRUE)
    else:
        return(FALSE)
        
n=int(input('digite n: '))
a=[]
for r in range(0,n,1):
    x=int(input('digite: '))
    a.append(x)
b=[]
for r in range(0,n,1):
    x=int(input('digite: '))
    b.append(x)
if lecker(a):
    print('S')
else:
    print('N')
if lecker(b):
    print('S')
else:
    print('N')
    
        

