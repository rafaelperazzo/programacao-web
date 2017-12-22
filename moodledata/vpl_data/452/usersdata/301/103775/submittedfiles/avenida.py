# -*- coding: utf-8 -*-
a=[]
n=int(input(' digite o valor de linhas:  '))
m=int(input(' digite o valor das colunas:  '))
for i in range(0,n,1):
   
    b=[]
    for j in range(0,m,1):
         a.append(int(input('digite o valor das colunas%d: '%(i+1))))
print(a)
