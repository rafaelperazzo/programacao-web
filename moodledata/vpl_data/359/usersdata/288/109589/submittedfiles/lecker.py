# -*- coding: utf-8 -*-
n=int(input("Digite a quantidade de termos da lista: "))
l=[]
m=[]
for i in range (0,n,1):
    l.append(int(input("Digite um termo para l: ")))
for i in range (0,n,1):
    m.append(int(input("Digite um valor para m: ")))
a=0
for i in range (0,n-2,1):
    if l[i]<l[i+1]>[i+2]:
        a+=1
if l[0]>l[1] or l[n-1]>l[n-2]:
    a+=1
    
if a==1:
    print ("SIM")
else:
    print ("NÃO")

b=0
for i in range (0,n-2,1):
    if m[i]<m[i+1]>[i+2]:
        b+=1
if m[0]>m[1] or m[n-1]>m[n-2]:
    b+=1
    
if b==1:
    print ("SIM")
else:
    print ("NÃO")

