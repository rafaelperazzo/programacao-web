# -*- coding: utf-8 -*-
def lecker(lista,n,p,v):
    p = 0
    v = 0
    for i in range(n-1):
        if lista[i-1] < lista[i] and lista[i] > lista[i+1]:
            p = p+1
        elif lista[i-1] > lista[i] and lista[i] < lista[i+1]:
            v = v+1
            break
    if p == 1 and v == 0:
        return True
    else:
        return False
n = int(input())
lista = []
lista2 = []
for i in range(n):
    lista.append(int(input()))
for i in range(n):
    lista2.append(int(input()))
if lecker(lista,n,0,0):
    print('S')
else:
    print('N')
if lecker(lista2,n,0,0):
    print('S')
else:
    print('N')        







'''
n = int(input())
lista = []
lista2 = []
for i in range(n):
    lista.append(int(input()))
p = 0
for i in range(n-1):
    if i >=1 and i <= n-2:
        if lista[i+1] > lista[i] and lista[i+1] > lista[i+2]:
            p = p+1
for i in range(n):
    lista2.append(int(input()))
p2 = 0
for i in range(n-1):
    if i > 0 :
        if lista2[i] > lista2[i+1] and lista2[i] > lista2[i-1]:
            p2 = p2+1
    if i == 0:    
        if lista2[i] > lista2[i+1]:
            p2 = p2+1
if p == 1:
    print('S')
else:
    print('N')
if p2 == 1:
    print('S')
else:
    print('N')
        
'''
