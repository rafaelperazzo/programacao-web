# -*- coding: utf-8 -*-

def pico(n,lista):
    #CONTINUE...
    for i in range(0,n-1,1):
        p = 0
        h = 0
        if lista[i]<lista[i+1]:
            continue
        else:
            p = i
            break
    for t in range(p,n-1,1):
        if lista[t]<lista[t+1]:
            continue
        else:
            h = h + 1
            break
    if h == 1:
        return False
    else:
        return True
                
              
                
        

#CONTINUE...

n = int(input('Digite a quantidade de elementos da lista: '))
a = []
for i in range(0,n,1):
    a.append(int(input('Digite um elemento de a: ')))

if pico(n,a):
    print('S')
else:
    print('N')
