# -*- coding: utf-8 -*-
def pico(lista):
    maior=0
    for i in range(0,len(lista),1):
        if lista[i]>maior:
            maior=lista[i]
            a=i
            b=i
        for i in range(1,b-1,1):
            if b==i:
                if lista[a]>lista[a-b] and lista[a]>lista[a+b]:
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
