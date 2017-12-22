# -*- coding: utf-8 -*-
n = int(input('informe a quantidade de elementos: '))

#lista 1
a =[]
for i in range (0,n,1):
    a.append(int(input('informe o %.d° elemento da lista1: '   %(i + 1))))
print(a)
#lista 2
'''
b = []
for i in range (0,n,1):
    b.append(int(input('informe o %.d° elemento da lista2: '   %(i + 1))))
print(b)

#lista 3

c = []
for i in range (0,n,1):
    c.append(int(input('informe o %.d° elemento da lista3: '   %(i + 1))))
print(c)
'''
#crescente e decrescente 
soma = 0
for i in range (0,len(a),1):
    if a[len(a)-1] > a[len(a)- 2]:
        soma = soma + 1
    else:
        print('N')
        break
if soma == len(a):
    print('S')
   
'''
for i in range (0,len(b),1):
    if b[0] > b[1]:
        print('N')
        break
    if b[i] < b[i+1]:
        print('S')
        break
for i in range (0,len(b),1):
    if c[0] > c[1]:
        print('N')
        break
    if c[i] < c[i+1]:
        print('S')
        break
'''
            


    