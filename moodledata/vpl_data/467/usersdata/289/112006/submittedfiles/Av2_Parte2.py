# -*- coding: utf-8 -*-
n=int(input("Digite a quantidade de elementos da lista a: "))
m=int(input("Digite a quantidade de elementos da lista b: "))
a=[]
for i in range(0,n,1):
    a.append(int(input("Digite o elemento%.d da lista a: " %(i+1))))
b=[]
for i in range(0,m,1):
    b.append(int(input("Digite o elemento%.d da lista b: " %(i+1))))
cont=0
for i in range(0,n,1):
    for i in range(0,m,1):
        if a[i]==b[i]:
            cont+=1
    print(cont)
