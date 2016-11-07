# -*- coding: utf-8 -*-
from __future__ import division
def lecker(l):
    cont=0
    for i in range(0,len(l),1):
        if i==0:
            if l[0]>l[1]:
                cont=cont+1
        if i==(len(l)-1):
            if l[i] > l[i-1]:
                cont =cont +1
        if i>0 and i<(len(l)-1):
            if l[i]>l[i-1] and l[i]>l[i+1]:
                cont=cont+1
    if cont==1:
        return True
    else:
        return False
n=input('Insira n:')
a=[]
b=[]
for i in range (0,n,1):
    a.append(input('Insira os valores de a:'))
for i in range (0,n,1):
    b.append(input('Insira os valores de b:'))
if lecker(a):
    print ('S')
else:
    print ('N')
if lecker(b):
    print ('S')
else:
    print('N')