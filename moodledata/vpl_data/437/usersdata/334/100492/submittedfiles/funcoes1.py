# -*- coding: utf-8 -*-

def crescente (a):
    c = 0
    for i in range (0,len(a)-1,1):
        if a[i] < a[i+1]:
            c += 1
        if c == len(a)-1:
            return 'S'
        else:
            return 'N'

def decrescente (a):
    c = 0
    for i in range (0,len(a)-1,1):
        if a[i] > a[i+1]:
            c += 1
        if c == len(a)-1:
            return 'S'
        else:
            return 'N'

def iguais (a):
    c = 0
    for i in range (0,len(a)-1,1):
        if a[i] == a[i+1]:
            c += 1
        if c>0:
            return 'S'
        else:
            return 'N'

#escreva o programa principal

n = int(input())
a = []
for i in range (0,6,1):
    a.append(int(input()))
b = []
for i in range (0,6,1):
    b.append(int(input()))
c = []
for i in range (0,6,1):
    c.append(int(input()))

print(crescente(a))
print(decrescente(a))
print(iguais(a))

print(crescente(b))
print(decrescente(b))
print(iguais(b))

print(crescente(c))
print(decrescente(c))
print(iguais(c))





