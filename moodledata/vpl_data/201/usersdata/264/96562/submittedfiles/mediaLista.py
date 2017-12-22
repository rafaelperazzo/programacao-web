# -*- coding: utf-8 -*-
n= int(input('Digite a quantidade de valores da lista:'))
a=[]
for i in range(0,n,1):
    valor=int(input('Digite o valor de cada termos da lista:'))
    a.append (valor)
    
print ('%.2f' %a[0])
print ('%.2f' %a[len(a)-1])

soma=0
for i in range (0,len(a),1):
    soma= a[i]+soma
media=soma/len(a)
print ('%.2f' %media)
print(a)