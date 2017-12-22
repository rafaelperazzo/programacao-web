# -*- coding: utf-8 -*-
def lecker(a,b,c):
    if a<b>c:
        return True
    elif a>b>c:
        return True
    elif a<b<c:
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
    
    
for i in range(0,n-1,1):
    if lecker(a[i-1],a[i],a[i+1]):
        conta=conta+1
if conta==n-2:
    print('S')
    
else:
    print('N')
    
for i in range(0,n-1,1):
    if lecker(b[i-1],b[i],b[i+1]):
        contb=contb+1
if contb==n-2:
    print('S')
    
else:
    print('N')