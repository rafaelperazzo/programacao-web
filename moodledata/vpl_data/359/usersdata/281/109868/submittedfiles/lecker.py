# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de termos: '))
l=[]

for i in range(0,n,1):
    l.append(int(input('Digite o valor da lista: ')))
    
c=0
if l[1]>l[0] and l[1]>l[2]:
    c=c+1
c1=0
if l[n-2]>l[n-1] and l[n-2]>l[n-3]:
    c1=c1+1
c2=0
for i in range(1,n-1,1):
    if l[i]>l[i+1] and l[i]>l[i-1]:
        c2=c2+1
        
l2=[]

for i in range(0,n,1):
    l2.append(int(input('Digite o valor da lista 2: ')))
    
c3=0
if l2[1]>l2[0] and l2[1]>l2[2]:
    c3=c3+1

c4=0
if l2[n-2]>l2[n-1] and l2[n-2]>l2[n-3]:
    c4=c4+1

c5=0
for i in range(1,n-1,1):
    if l2[i]>l2[i+1] and l2[i]>l2[i-1]:
        c5=c5+1

if c==0 or c1==0 or c2==0:
    print('S')
else:
    print('N')
if c==3 or c1==4 or c2==5:
    print('S')
else:
    print('N')