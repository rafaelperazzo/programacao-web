# -*- coding: utf-8 -*-

def pmax(n):
    cont=0
    for i in range (0,len(n)-1,1):
        if n[i]<n[i+1]:
            return (i)
def pico(n):
    x=pmax(n)
    for i in range (x,len(n)-1,1):
        if n[i]<n[i+1]:
            return False
    return True        
            

n =int(input('Digite a quantidade de elementos da lista: '))
a=[]
for i in range (1,n+1,1):
    valor=int(input('Digite o elemento da lista: '))
    a.append(valor)
if pico(n):
    print('S')
else:
    print('N')
