# -*- coding: utf-8 -*-

def pico(n,lista):
    #CONTINUE...
    for i in range(0,n-1,1):
        p = 0
        if lista[i]<lista[i+1]:
            continue
        else:
            p = lista[i]
            break
        for t in range(p,n-1,1):
            h = 0
            if lista[t]<lista[t+1]:
                h = h + 1
            elif lista[t]>lista[t+1]:
                h = h - 100000000000
    if h>0:
        return True
    else:
        return False
                
              
                
        

#CONTINUE...

n = int(input('Digite a quantidade de elementos da lista: '))
a = []
for i in range(0,n,1):
    a.append(int(input('Digite um elemento de a: ')))

if pico(n,a):
    print('S')
else:
    print('N')
