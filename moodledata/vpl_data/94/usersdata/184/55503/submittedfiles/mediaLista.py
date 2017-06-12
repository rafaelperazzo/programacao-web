# -*- coding: utf-8 -*-
soma=0
a=[]
for i in range(0,len(a),1):
    soma=soma+lista[i]
media=soma/n
n=int(input('digite a quantidade de elementos:'))
for i in range(0,n,1):
    num=float(input('digite um valor:'))
    a.append(num)
print(media)