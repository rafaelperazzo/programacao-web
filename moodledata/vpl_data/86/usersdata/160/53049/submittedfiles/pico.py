# -*- coding: utf-8 -*-

def pico(n):
    #CONTINUE...
    cont=0
    for i in range(0,len(n)-1,1):
        if n[i]<n[i]>n[i]:
            cont=cont+1

n = int(input('Digite a quantidade de elementos da lista: '))
#CONTINUE...

a=[]
for i in range(1,n+1,1):
    valor=int(input('Digite o elementos da lista:'))
    a.append(valor)
    
if pico(a):
    print('S')
    
else:
    print('N')
    