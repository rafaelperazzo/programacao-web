# -*- coding: utf-8 -*-

def pico(lista,n):
    status=str('none')
    c=0
    v=0
    for i in range (0,n-1,1):
        if lista[i] < lista[i+1]:
            c=c + 1
        else:
            v=i
            break
    for i in range (v,n-1,1):
        if lista[i] > lista[i+1]:
            c=c+1
        else:
            break
    if c == (n-1):
        status=str('S')
    else:
        status=str('N')
    return(str(status))
    
a=[]
n = int(input('Digite a quantidade de elementos da lista: '))
for i in range (0,n,1):
    a.append(int(input('Digite o termo %d: ' %(i+1))))
print(pico(a,n))    
