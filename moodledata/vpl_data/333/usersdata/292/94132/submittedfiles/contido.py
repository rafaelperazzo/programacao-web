# -*- coding: utf-8 -*-
def q_in(b, a):
    cont = 0
    for i in b:
        if i in a:
            cont += 1
    return cont
############ - PROGRAMA PRINCIPAL - ##########
na = int(input("Digite a quantidade de elementos de a: "))
nb = int(input("Digite a quantidade de elementos de b: "))
a, b = [], []
for i in range(1, na+1):
    a.append(int(input("Digite o %d elemento de a: "%i)))
for i in range(1, nb+1):
    b.append(int(input("Digite o %d elemento de b: "%i)))
print(q_in(b, a))