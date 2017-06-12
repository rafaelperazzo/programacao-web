# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de números na lista:'))
a=[]
b=[]

for i in range(0,n,1):
    c=int(input('Digite um valor para lista h:'))
    a.append(c)
    
for i in range(0,n,1):
    d=int(input('Digite um valor para lista b:'))
    b.append(d)

def lecker(x):
    cont=0
    for i in range(0,len(x),1):
        if i==0:    
            if (a[i])>(a[i+1]):
                cont=cont+1
            i=i+1
        elif (i==(len(a)-1)):
            if (a[i])>(a[i-1]):
                cont=cont+1
        else:
            if (a[i])>(a[i+1]) and (a[i])>(a[i-1]):
                cont=cont+1
            i=i+1
        if cont==1:
            return True
        else:
            return False
if lecker(h):
    print('S')
else:
    print('N')

if lecker(b):
    print('S')
else:
    print('N')

print(b)
print(h)