# -*- coding: utf-8 -*-
n=int(input("Digite a ordem da matriz:"))
m=[]

for i in range(0,n,1):
    l=[]
    for j in range(0,n,1):
        l.append(int(input("Digite o elemento%.d" %(i+1))))
    m.append(l)
print(m)