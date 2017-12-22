# -*- coding: utf-8 -*-
m=int(input("Digite a quantidade de de elementos de a: "))
n=int(input("Digite a quantidade de de elementos de b: "))
a=[]
b=[]
for i in range(0,n,1):
    a.append(int(input("Digite número%.d:" %(i+1))))
for i in range(0,m,1):
    b.append(int(input("Digite número%.d:" %(i+1))))
c=0
for i in range (0,n-1,1):
    for j in range(0,m-1,1):
        if a[i]==b[j]:
            c+=1
print(c)