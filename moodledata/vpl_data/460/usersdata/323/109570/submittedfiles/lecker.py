# -*- coding: utf-8 -*-
def lecker(a,b,c):
    if a<b and b>c:
        return True

a=[]
b=[]
conta=0
contb=0

n=int(input('Digite a quantidade de elementos da lista: '))

for i in range(0,n,1):
    valor_a=float(input('Digite o elemento da lista: '))
    a.append(valor_a)
for i in range(0,n,1):
    valor_b=float(input('Digite o elemento da lista: '))
    b.append(valor_b)
    
    
for i in range(0,n,1):
    if i==0:
        if a[i]>a[i+1]:
            conta=conta+1
        elif i==n-1:
            if a[n-1]>a[n-2]:
                conta=conta+1
        else:
            if lecker(a[i-1],a[i],a[i+1]):
                conta= conta+1       
if conta==1:
    print('S')
    
else:
    print('N')
    
for i in range(0,n,1):
    if i==0:
        if b[i]>b[i+1]:
            contb=contb+1
        elif i==n-1:
            if b[n-1]>b[n-2]:
                contb=contb+1
        else:
            if lecker(b[i-1],b[i],b[i+1]):
                contb= contb+1       
if contb==1:
    print('S')
    
else:
    print('N')