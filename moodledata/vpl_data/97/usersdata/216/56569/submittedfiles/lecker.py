# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de números na lista:'))
h=[]
b=[]

for i in range(0,n,1):
    c=int(input('Digite um valor para lista h:'))
    h.append(c)
    
for i in range(0,n,1):
    d=int(input('Digite um valor para lista b:'))
    b.append(d)

def lecker(a):
    cont=0
    i=0
    while i>len(a):
        if i==0:    
            if (a[i])>(a[i+1]):
                cont=cont+1
                i=i+1
        elif (i==(len(a)-1)):
            if (a[i])>(a[len(a)-1]):
                cont=cont+1
        else:
            if (a[i])>(a[i+1]) and (a[i])>(a[i-1]):
                cont=cont+1
                i=i+1

        return(cont)
    
if (lecker(h)==1):
    print('S')
else:
    print('N')

if (lecker(b)==1):
    print('S')
else:
    print('N')

print(b)
print(h)