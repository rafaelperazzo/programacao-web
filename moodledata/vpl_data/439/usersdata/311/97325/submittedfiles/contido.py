# -*- coding: utf-8 -*-
n=int(input('Digite o numero: '))
a=[]
b=[]

for i in range (0,n,1):
    a.append(input('Digite o numero%d: ' %(i+1)))
for i in range (0,n,1):
    b.append(input('Digite o numero%d: ' %(i+1)))

for z in a:
    contagem=0
    for w in b:
        if z==w:
            contagem+=1
    print(contagem)


    

    

