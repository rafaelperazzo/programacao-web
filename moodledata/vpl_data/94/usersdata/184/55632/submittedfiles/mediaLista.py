# -*- coding: utf-8 -*-
soma=0
a=[]
n=int(input('digite a quantidade de elementos:'))
for i in range(0,n,1):
    num=float(input('digite um valor:'))
    a.append(num)
for i in range(0,len(a),1):
    soma=soma+a[i]
media=soma/n
print('%.2f'%a[0])
print('%.2f'%a[n-1])
print('%.2f'%media)
print(a)