# -*- coding: utf-8 -*-
a=[]
b=[]
c=[]
n=int(input('Digite o número de elementos: '))
while n<=0:
    print('Número inválido!')
    n=int(input('Digite o número de elemento: '))
for i in range(0,n,1):
    a.append(input('Digite um elemento para a: '))
for j in range(0,n,1):
    b.append(input('Digite um elemento para b: '))
for k in range(0,n,1):
    c.append(input('Digite um elemento para c: '))
