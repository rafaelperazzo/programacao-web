# -*- coding: utf-8 -*-
n=int(input('Digite o numero: '))
a=[]
b=[]

for i in range (0,n,1):
    a.append(input('Digite o numero%d: ' %(i+1)))
for i in range (0,n,1):
    b.append(input('Digite o numero%d: ' %(i+1)))

c=a+b
for z in c:
    contagem=0
    for w in c:
        if z==w:
            contagem+=1
    print('ha %d vslores iguais a %d' % (contagem, z))


    

    

