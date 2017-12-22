# -*- coding: utf-8 -*-
a=[]
b=[]

n=int(input('Digite o tamanho de a:'))
m=int(input('Digite o tamanho de b:'))

for i in range(0,n,1):
    a.append(int(input('Digite os elementos de a: ')))
for j in range(0,m,1):
    b.append(int(input('Digite os elementos de b: ')))
    
if len(a)<len(b):
    menor=len(a)
    elem=a[i]
    
else :
    menor=len(b)
    elem=b[i]
   
if menor=len(a):
    teste=a
else:
    teste=b


cont=0


for i in range(0,menor,1):
    if elem in a:
        cont+=1
    
        
        
print(cont)
    