# -*- coding: utf-8 -*-

def pico(lista,n):
    status=str("none")
    var0=0
    var1=0
    for i in range (0,n-1,1):
        if lista[i] < lista[i+1]:
            status=str("N")
        else:
            if lista[i] > lista[i+1] and lista[n-1] < lista[n-2]:
                status=str("S")
            else:
                status=str("N")
    return(str(status))


a=[]
n = int(input('Digite a quantidade de elementos da lista: '))
for i in range (0,n,1):
    a.append(int(input("Digite o termo %d: " %(i+1))))
print(pico(a,n))
