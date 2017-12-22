# -*- coding: utf-8 -*-
n=int(input("Digite a quantidade de elementos da lista a:"))
m=int(input("Digite a quantidade de elementos da lista b:"))
a=[]
for i in range(0,n,1):
    a.append(int(input("Digite o elemento%.d da lista a" %(i+1))))
print(a)

