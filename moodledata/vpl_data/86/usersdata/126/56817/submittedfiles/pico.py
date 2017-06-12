# -*- coding: utf-8 -*-

def pico(a):
    cont=0
    cont1=0
    i=0
    for i in range(0,len(a),1):
        while a[i]<a[i+1]:
            cont=cont+1
        i=i+1
    for i in range(cont,len(a),1):
        if a[i]>a[i+1]:
            cont1=cont1+1
        i=i+1
    if cont1==(range(cont,len(a))):
        return(cont1)
   

n = int(input('Digite a quantidade de elementos da lista: '))
b=[]
i=0
for i in range(0,n,1):
    p=int(input('digite um valor:'))
    b.append(p)
    i=i+1
print(pico(b)
if pico(b):
    print('S')
else:
    print('N')
