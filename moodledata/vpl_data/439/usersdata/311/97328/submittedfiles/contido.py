# -*- coding: utf-8 -*-
n=int(input('Digite o numero: '))
m=int(input('Digite o numero: '))
a=[]
b=[]

for i in range (0,n,1):
    a.append(input('Digite o numero%d: ' %(i+1)))
for i in range (0,m,1):
    b.append(input('Digite o numero%d: ' %(i+1)))

contagem=0
for z in a:
    for w in b:
        if z==w:
            contagem+=1
print(contagem)


    

    

