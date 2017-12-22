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
soma = 0
for i in range (0,len(a),1):
    
    if a[i] > a[i +1]:
        soma = soma + 1
    else:
        print('N')
        break
if soma == len(a):
    print('S')
s = 0
for i in range (0,len(a),1):
    if a[len(a) - 1] < a[len(a) - 2]:
        s = s + 1
    else:
        print('N')
        break
if s == len(a):
    print('S')
soma = 0
#crescente decrescente b
#decrescente b
for i in range (0,len(b),1):
    
    if a[len(b)-1] > a[len(b)- 2]:
        print("S")
    else:
        print('N')
        break

    
#crescente
for i in range (0,len(b),1):
    s  = 0
    if a[len(b) - 1] < a[len(b) - 2]:
        print('S')
    else:
        print('N')
        break

#crescente decrescente c
for i in range (0,len(c),1):
    
    if a[len(c)-1] > a[len(c)- 2]:
        soma = soma + 1
    else:
        print('N')
        break
if soma == len(c):
    print('S')
    

for i in range (0,len(c),1):
    s  = 0
    if a[len(c) - 1] < a[len(c) - 2]:
        s = s + 1
    else:
        print('N')
        break
if s == len(c):
    print('S')

            


    