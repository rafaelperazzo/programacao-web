# -*- coding: utf-8 -*-
a = int(input('insira a quantidade de elementos em a: '))
b = int(input('insira a quantidade de elementos em b: '))
ele_a = []
ele_b = []
for i in range(0,a,1):
    ele_a.append(int(input('digite os elementos de a: ')))
print(ele_a)
for i in range(0,b,1):
    ele_b.append(int(input('digite os elementos de b: ')))
print(ele_b)
cont=0
if ele_b in ele_a:
    cont= cont + 1
else:
    cont=0
if cont==1:
    print('s')
else:
    print('n)