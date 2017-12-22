# -*- coding: utf-8 -*-

def comp(n,m):  
    cont= 0
    for i in range(0,len(n),1):
        for j in range(0,len(m),1):
            if n[i]==m[j]:
                cont +=1
    return cont
    
a= []
n= int(input('Digite um valor para n: '))
for i in range(0,n,1):
    a.append(int(input('Digite um valor: ')))
   
b= []
m= int(input('Digite um valor para m: '))
for i in range(0,m,1):
    b.append(int(input('Digite um valor: ')))

print (comp(a,b))
    
