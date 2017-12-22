# -*- coding: utf-8 -*-
n1=int(input())
n2=int(input())
n3=int(input())
lista1=[]
lista2=[]
lista3=[]
c=0
e=0

for i in range (0,n,1) :
     lista1.append(int(input()))
for i in range (0,n-1,1) :
    if lista1[i] < lista1[i+1] :
        c+=1
    if lista1[i] == lista1[i+1] :
        e+=1
if c==(n-1) :
    print('S')
    print('N')
    print('N')
else :
    if c==0 and e==0 :
        print('N')
        print('S')
        print('N')
    else :
        if e > 0 :
            print('N')
            print('N')
            print('S')
        else :
           print('N')
           print('N')
           print('N')
for i in range (0,n,1) :
     lista2.append(int(input()))
for i in range (0,n-1,1) :
    if lista2[i] < lista2[i+1] :
        c+=1
    if lista2[i] == lista2[i+1] :
        e+=1
if c==(n-1) :
    print('S')
    print('N')
    print('N')
else :
    if c==0 and e==0 :
        print('N')
        print('S')
        print('N')
    else :
        if e > 0 :
            print('N')
            print('N')
            print('S')
        else :
           print('N')
           print('N')
           print('N')
