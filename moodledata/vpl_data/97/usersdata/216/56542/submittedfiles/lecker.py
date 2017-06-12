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

def leker(a):
    cont=0
    for i in range(0,len(a),1):
        if (a[i])>(a[i+1]):
            cont=cont+1
        if (a[i])>(a[i+1]) and (a[i])>(a[i-1]):
            cont=cont+1
        if (a[len(a)-1])>(a[len(a)-2]):
            cont=cont+1
    if cont==1:
        return True
    else:
        return False



print(leker(h))
