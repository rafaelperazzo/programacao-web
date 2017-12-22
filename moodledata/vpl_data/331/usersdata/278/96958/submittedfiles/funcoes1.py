# -*- coding: utf-8 -*-

def crescente (lista):
    #escreva o código da função crescente aqui
    c=0
    for i in range (0,n,1):
        b=i+1
        lista[i]<lista[b]:
            continue
        else:
            c+=1
            break
    return c

#escreva as demais funções





#escreva o programa principal
n = int(input("Digite a quantidade de elementos: "))
lista1 = []
lista2 = []
lista3 = []
for i in range (0,n,1):
    lista1.append(float(input("Digite número%.d da lista 1: " %(i+1))))
    lista2.append(float(input("Digite número%.d da lista 2: " %(i+1))))
    lista3.append(float(input("Digite número%.d da lista 3: " %(i+1))))
x = crescente (lista1)
y = crescente (lista2)
z = crescente (lista3)
if x==0:
    print("S")
else:
    print("N")
if y==0:
    print("S")
else:
    print("N")
if z==0:
    print("S")
else:
    print("N")