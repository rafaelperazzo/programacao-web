# -*- coding: utf-8 -*-

def pico(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if a[i]<a[i+1]:
            cont=cont+1
        y=len(lista)/2
    for i in range(0,len(lista)-1,1):
        if i>=y:
            if a[i]>a[i+1]:
                cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False
            
    
n = input('Digite a quantidade de elementos da lista: ')

a=[]
for i in range(1,n+1,1):
    a=int(input('Digite os valores:'))
    a.append(a)

if pico(a):
    print('S')
else:
    print('N')