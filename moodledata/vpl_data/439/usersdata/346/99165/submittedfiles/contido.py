# -*- coding: utf-8 -*-

def comp(n,m):  
    cont= 0
    for i in range(0,len(n),1):
        for j in range(0,len(m),1):
            if n[i]==m[j]:
                cont +=1
    return cont
'''    
a= []
n= int(input('Digite um valor para n: '))
for i in range(0,n,1):
    a.append(int(input('Digite um valor: ')))
   
b= []
m= int(input('Digite um valor para m: '))
for i in range(0,m,1):
    b.append(int(input('Digite um valor: ')))
'''
n=10
m=4
a=[1,2,3,4,5,6,7,8,9,10]
b=[5,9,18,20]

print (comp(a,b))
    
c=7
d=5
e=[22,11,10,8,12,76,50]
f=[9,76,20,21]

print(comp(e,f))