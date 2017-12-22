# -*- coding: utf-8 -*-
n=int(input("Digite a quantidade de termos da lista: "))
l=[]
m=[]
for i in range (0,n,1):
    l.append(int(input("Digite um termo para l: ")))
for i inrange (0,n,1):
    m.append(int(input("Digite um valor para m: ")))
a=0
for i in range (0,n-2,1):
    if l[1]<l[i+1]>[i+2]:
        a+=1
    elif l[1]>l[1+1] or l[n-1]>l[n-2]:
        a+=1
        


