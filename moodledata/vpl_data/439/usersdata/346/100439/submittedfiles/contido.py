# -*- coding: utf-8 -*-

def comp(n,m):  
    cont= 0
    for i in range(0,len(a),1):
        for j in range(0,len(b),1):
            if a[i]==b[j]:
                cont += 1
    return cont

a= []
n= int(input())
for i in range(0,n,1):
    a.append(int(input('Digite um valor: ')))
   
b= []
m= int(input())
for i in range(0,m,1):
    b.append(int(input('Digite um valor: ')))


print (comp(a,b))
    
