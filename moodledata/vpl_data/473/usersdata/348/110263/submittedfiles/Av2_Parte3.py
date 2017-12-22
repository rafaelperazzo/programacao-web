# -*- coding: utf-8 -*-
n = int(input('informe a quantidade de elementos: '))

#lista 1
a =[]
for i in range (0,n,1):
    a.append(int(input('informe o %.d° elemento da lista1: '   %(i + 1))))
print(a)
#lista 2

b = []
for i in range (0,n,1):
    b.append(int(input('informe o %.d° elemento da lista2: '   %(i + 1))))
print(b)

#lista 3

c = []
for i in range (0,n,1):
    c.append(int(input('informe o %.d° elemento da lista3: '   %(i + 1))))
print(c)

#crescente e decrescente a

for i in range (0,n,1):
    if a[i] < a[i +1]:
        print('S')
        break
    else:
        print('N')

for i in range (0,n,1):
    if a[i] > a[i+1]:
        print('S')
        break
    else:
        print('N')
        break
#crescente decrescente b        
        
for i in range (0,n,1):
    if b[i] < b[i +1]:
        print('S')
        break
for i in range (0,n,1):
    if b[i] > b[i+1]:
        print('S')
        break
    else:
        print('N')

#crescecnet c

for i in range (0,n,1):
    if c[i] < c[i +1]:
        print('S')
        break
for i in range (0,n,1):
    if c[i] > c[i+1]:
        print('S')
        break
    else:
        print('N')


            


    