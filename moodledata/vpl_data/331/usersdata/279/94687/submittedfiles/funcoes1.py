# -*- coding: utf-8 -*-
n=int(input())

lista1=[]
lista2=[]
lista3=[]
c1=0
e1=0
c2=0
e2=0
c3=0
e3=0
for i in range (0,n,1) :
     lista1.append(int(input()))
for i in range (0,n-1,1) :
    if lista1[i] < lista1[i+1] :
        c1+=1
    if lista1[i] == lista1[i+1] :
        
        e1+=1
for i in range (0,n,1) :
     lista2.append(int(input()))
for i in range (0,n-1,1) :
    if lista2[i] < lista2[i+1] :
        c2+=1
    if lista2[i] == lista2[i+1] :
        e2+=1
for i in range (0,n,1) :
     lista3.append(int(input()))
for i in range (0,n-1,1) :
    if lista3[i] < lista3[i+1] :
        c3+=1
    if lista3[i] == lista3[i+1] :
        e3+=1        
if c1==(n-1) :
    print('S')
    print('N')
    print('N')
else :
    if c1==0 and e1==0 :
        print('N')
        print('S')
        print('N')
    else :
        if e1 > 0 :
            print('N')
            print('N')
            print('S')
        else :
           print('N')
           print('N')
           print('N')

if c2==(n-1) :
    print('S')
    print('N')
    print('N')
else :
    if c2==0 and e2==0 :
        print('N')
        print('S')
        print('N')
    else :
        if e2 > 0 :
            print('N')
            print('N')
            print('S')
        else :
           print('N')
           print('N')
           print('N')

if c3==(n-1) :
    print('S')
    print('N')
    print('N')
else :
    if c3==0 and e3==0 :
        print('N')
        print('S')
        print('N')
    else :
        if e3 > 0 :
            print('N')
            print('N')
            print('S')
        else :
           print('N')
           print('N')
           print('N')
