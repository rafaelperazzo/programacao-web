# -*- coding: utf-8 -*-

def pico(a):
    cont=0
    cont1=0
    i=0
    for i in range(0,len(a),1):
        if a[i]<a[i+1]:
            cont=cont+1
        else:
            break
        i=i+1
    for i in range(cont,len(a)-1,1):
        if a[i]>a[i+1]:
            cont1=cont1+1
        i=i+1
    if (len(a)-1)-cont1==cont and (len(a)-1)-cont==cont1:
        return  True
   

n = int(input('Digite a quantidade de elementos da lista: '))
b=[]
i=0
for i in range(0,n,1):
    p=int(input('digite um valor:'))
    b.append(p)
    i=i+1
if pico(b):
    print('S')
else:
    print('N')
