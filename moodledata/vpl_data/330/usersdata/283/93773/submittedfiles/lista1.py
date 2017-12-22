# -*- coding: utf-8 -*-

n=int(input('Digite a quantidade de números: '))
a=[]
soma=0
for i in range(0,n,1):
    a.append(int(input('Digite um valor: ')))
    if(a[i]%2==0):
        soma += a[i]
        break
        print('soma dos pares: %d' %soma)
        
