# -*- coding: utf-8 -*-
'''a=[]
b=[]
for i in range (3):
    for j in range (3):
        if tabuleiro[i][j]==simbH:
            a.append(i)
            a.append(j)
        if tabuleiro[i][j]==simbM:
            b.append(i)
            b.append(j)

if a[0]==a[1] and a[2]==a[3]:
    k=3-(a[0]+a[2])
    if tabuleiro[k][k]==" ":
        tabuleiro[k][k]=simbM
if a[0]==a[2]:
    f=a[0]
    k=3-(a[1]+a[3])
    if tabuleiro[f][k]==" ":
        tabuleiro[f][k]=simbM
if a[1]==a[3]:
    f=a[1]
    k=3-(a[1]+a[3])
    if tabuleiro[k][f]==" ":
        tabuleiro[k][f]=simbM
if (a[1]+a[0])==2 and (a[2]+a[3])==2:
    k=3-(a[0]+a[2])
    f=3-(a[1]+a[3])
    tabuleiro[k][f]=simbM'''
x= int(input("x:"))   
k=  int(input("k:"))   
if x==0:
    if k==1:
    break
    x=7
print (x)

        
    