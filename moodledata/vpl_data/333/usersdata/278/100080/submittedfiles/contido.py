# -*- coding: utf-8 -*-
na = int(input("Digite a quantidade de elementos da lista a: "))
nb = int(input("Digite a quantidade de elementos da lista b: "))
a = []
for i in range (0,na,1):
    a.append(int(input("Digite o elemento%.d da lisat a: " %(i+1))))
b = []
for i in range (0,nb,1):
    b.append(int(input("Digite o elemento%.d da lista b: " %(i+1))))
c=0
for i in range (0,na,1):
    for j in range (0,nb,1):
        if a[i]==b[j]:
            c+=1
print(c)
