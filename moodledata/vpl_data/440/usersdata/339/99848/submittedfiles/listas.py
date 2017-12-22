# -*- coding: utf-8 -*-

def degrau(lista):
    h=[]
    for i in range(0,len(lista)-1):
        h.append(int(lista[i+1]-lista[i]))
    print (h)
    
n=int(input('quantidade de elementos: '))
a=[]

while n<2:
    print('tente novamente !')
    n=int(input('quantidade de elementos: '))

for i in range(0,n):
    a.append(int(input('elementos para a: ')))

degrau(a)
