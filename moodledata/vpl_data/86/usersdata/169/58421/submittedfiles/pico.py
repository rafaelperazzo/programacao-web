# -*- coding: utf-8 -*-
n=int(input('Digite a Quantidade de Elementos da Lista:'))
l1=[]
for i in range(0,n,1):
    v=int(input('Digite os Elementos da Lista:'))
    l1.append(v)

def pico(n):
    if n[0]<n[1]:
        i=0
        cont=1
        while cont<n:
            if i==0:
                if n[cont]<n[cont-1]
                i=1
            elif i==1:
                if n[cont]>n[cont-1]
                i=2
            else:
                return False
            cont=cont+1
        return True
    else: 
        return False

if pico(n):
    print('S')
else: 
    print('N')
    
