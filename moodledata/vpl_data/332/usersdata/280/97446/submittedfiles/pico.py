# -*- coding: utf-8 -*-

def pico(lista,n):
    status=str("none")
        for i in range (0,n-1,1):
            if lista[i] < lista[i+1]:
                status=str("S")
            else:
                if lista[i] > lista[i+1]:
                    status=str("S")
                else:
                    status=str("N")
    return(status)


a=[]
n = input('Digite a quantidade de elementos da lista: ')
for i in range (0,n,1):
    a.append(int(input("Digite o termo %d: " %(i+1))))
print(pico(a,n))
