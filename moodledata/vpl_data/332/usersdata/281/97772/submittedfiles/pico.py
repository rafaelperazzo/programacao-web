# -*- coding: utf-8 -*-

def pico(lista):
    status=str('none')
    cont=0
    var0=0
    for i in range (0,n-1,1):
        if lista[i] < lista[i+1]:
            cont=cont + 1
        else:
            var0=i
            break
    for i in range (var0,n-1,1):
        if lista[i] > lista[i]:
            cont=cont+1
        else:
            break
    if cont == (n-1):
        status=str('S')
    else:
        status=str('N')
    return(str(status))
    
a=[]
n = int(input('Digite a quantidade de elementos da lista: '))
for i in range (0,n,1):
    a.append(int(input('Digite o termo %d: ' %(i+1))))
print(pico(a,n))    
