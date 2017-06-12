# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade:'))
h=[]
b=[]

for i in range(1,n+1,1):
    c=int(input('Digite um valor:'))
    h.append(c)
    
for i in range(1,n+1,1):
    d=int(input('Digite um valor:'))
    b.append(d)
    
def leker(a):
    cont=0
    for i in range(0,len(a)-1,1):
        if (a[i])>(a[i+1]) or (a[i])<(a[i+1]):
            cont=cont+1
    if cont==1:
        return True
    else:
        return False
    
    
    
print(h)
print(b)

if leker(h):
    print('S')
else:
    print('N')

if leker(b):
    print('S')
else:
    print('N')