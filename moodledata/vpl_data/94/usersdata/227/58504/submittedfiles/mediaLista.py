# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de elementos da lista:'))
a=[]

for i in range(1, n+1 , 1):
    a.append(int(input('Digite os valores da lista:')))
    
soma=0
for i in range  (0,len(a),1):
    soma=soma+a[i]
media=soma/len(a)
print('%.2f' %a[0])
print('%.2f' %a[len(a)-1])
print('%.2f' %media)
print(a)
