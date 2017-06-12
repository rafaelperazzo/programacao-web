# -*- coding: utf-8 -*-

def pico(lista):
    maior=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>maior:
            maior=lista[i]
            a=i
            b=i
    while a>=1:
        if lista[a]>lista[a-1]:
            a=a-1
    if a==1:
        esquerdo=1
    while b<=(len(lista)-1):
        if lista[b]<lista[b+1]:
            b=b+1
    if b==(len(lista)-1):
        direito=1
    if direito==1 and esquerdo==1:
        return True
    else:
        return False
        
L=[]
n = int(input('Digite a quantidade de elementos da lista: '))
for i in range(1,n+1,1):
    l=int(input('digite elemento: '))
    L.append(l)
if pico(L):
    print('S')
else:
    print('N')
