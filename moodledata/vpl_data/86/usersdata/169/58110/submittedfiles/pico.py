# -*- coding: utf-8 -*-

def pico(n):
    cont=0
    for i in range(0,len(n)-1,1):
        if n[i]<n[i+1]<n[i+2]:
            cont=cont+1
            return True
        else: 
            return False

n=int(input('Digite a Quantidade de Elementos da Lista:'))
l1=[]
for i in range(1,n+1,1):
    v=int(input('Digite os Elementos da Lista:'))
    l1.append(v)
if pico(l1)==True:
    print('S')
else:
    print('N')
    
