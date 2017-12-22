# -*- coding: utf-8 -*-

def pico(lista):
    c=0
    for i in range (0,n,1):
        if i<(n-1):
            if (lista[i]<lista[i+1]):
                continue
            else:
                c+=1
                break
        for i in range (i,n,1):
            if i<(n-1):
                if lista[i]>lista[i+1]:
                    continue
                c-=1
                if lista[i]<lista[i+1]:
                    c+=1
                    break
    return c


n = input('Digite a quantidade de elementos da lista: ')
lista = []
for i in range (0,n,1):
    lista.append(int(input("Digite número%.d da lista: " %(i+1))))
x = pico(lista)
if x==0:
    print("S")
if x==1:
    print("N")
