# -*- coding: utf-8 -*-
a=[]
b=[]
n=int(input("Digite a quantidades de elementos de a: "))
m=int(input("Digite a quantidades de elementos de b: "))
for i in range(0,n,1):
    a.append(int(input("Digite um elemento de a: ")))
for i in range(0,m,1):
    b.append(int(input("Digite um elemento de b: ")))
c=0
for i in range(0,n,1):
    if a[i] in b:
        c+=1
print(c)
        

    
    

