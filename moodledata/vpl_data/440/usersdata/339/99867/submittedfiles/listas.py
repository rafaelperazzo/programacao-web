# -*- coding: utf-8 -*-

def degrau(lista):
    h=[]
    for i in range(0,len(lista)-1):
        h.append(lista[i+1]-lista[i])
    for i in range(len(h)-1):
        if h[i]>=h[i+1] and h[i]>=h[i-1]:
            print (h[i])
        elif h[i]<=h[i+1] and h[i]>=h[i-1]:
            print (h[i+1])
        elif h[i-1]>=h[i] and h[i]>=h[i+1]:
            print (h[i-1])
    return
    
n=int(input('quantidade de elementos: '))
a=[]

while n<2:
    print('tente novamente !')
    n=int(input('quantidade de elementos: '))

for i in range(0,n):
    a.append(int(input('elementos para a: ')))

degrau(a)
