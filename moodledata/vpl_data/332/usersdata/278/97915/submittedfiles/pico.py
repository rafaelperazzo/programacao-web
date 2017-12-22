# -*- coding: utf-8 -*-

def pico(lista):
    c=0
    for i in range (0,n,1):
        if i<(n-1):
            if lista[i]<lista[i+1]:
                c+=1
                continue
            else:
                for i in range (c,n,1):
                    if i<(n-1):
                        if lista[i]>lista[i+1]:
                            continue
                        if lista[i]<lista[i+1]:
                            c*=0
                            break
        else:
            break
    return c


n = int(input('Digite a quantidade de elementos da lista: '))
lista = []
for i in range (0,n,1):
    lista.append(int(input("Digite número%.d da lista: " %(i+1))))
x = pico(lista)
y=n-1
if x>0:
    print("S")
if x==0 or x==y:
    print("N")
