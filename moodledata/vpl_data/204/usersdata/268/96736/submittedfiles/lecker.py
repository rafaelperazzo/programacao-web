# -*- coding: utf-8 -*-

def lecker(a):
    cont=0
    for i in range(0,n,1):
        if i==0:
            if a[1]<a[0]:
                cont=cont+1
        elif i==(n-1):
            if a[n-1]>a[n-2]:
                cont=cont+1
        else:
            if a[i]>a[i+1] and a[i]>a[i-1]:
                cont=cont +1
    if cont==1:
        return(1)
    else:
        return(0)
         


n=int(input('Digite a qtd de termo : '))
a=[]
b=[]

for i in range(0,n,1):
    valora=int(input('Digite a : '))
    a.append(valora)
for i in range(0,n,1):
    valorb=int(input('Digite b : '))
    b.append(valorb)
if lecker(a)==1:
    print('S')
if lecker(a)==0:
    print('N')
if lecker(b)==1:
    print('S')
if lecker(b)==0:
    print('N')


