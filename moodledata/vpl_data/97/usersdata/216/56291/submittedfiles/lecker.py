# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade:'))
a=[]
b=[]

for i in range(1,n+1,1):
    c=int(input('Digite um valor:'))
    a.append(c)
    
for i in range(1,n+1,1):
    d=int(input('Digite um valor:'))
    b.append(d)
    
def leker(x):
    cont=0
    for i in range(0,n+1,1):
        if a[i]>a[i+1]:
            cont=cont+1
    if cont==1:
        return True
    else:
        return False
    
    
    
print(a)
print(b)

if leker(a):
    print('S')
else:
    print('N')

if leker(b):
    print('S')
else:
    print('N')