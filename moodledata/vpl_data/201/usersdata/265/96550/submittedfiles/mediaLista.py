# -*- coding: utf-8 -*-
n=int(input('digite a quantidade de termos da lista: '))
a=[]
for i in range(0,n,1):
    valor=int(input('digite o valor da lista: '))
    a=[valor]
print('%.2f' %a[0])
print('%.2f' %a[len(a)-1])
soma=0
for i in range(0,len(a),1):
    soma=soma+a[i]
resultado=soma/len(a)
print('%2.f' %reslutado)
print(a)