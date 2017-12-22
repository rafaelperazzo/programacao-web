# -*- coding: utf-8 -*-
def lista (a, b):
    for i in range (0, b, 1):
        a.append(int(input('Digite: ')))
def q_element(a, b, c):
    som = 0
    for i in range (0, c, 1):
        if a[i] in b:
            som += 1
    return som
n = int(input('Digite a quantidade de "a": '))
m = int(input('Digite a quantidade de "b": '))
a = []
b = []
lista (a, n)
lista (b, m)
print (q_element (b, a, m))

