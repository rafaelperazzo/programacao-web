# -*- coding: utf-8 -*-
n=int(input(' Número de salas: '))
a=[]
for i in range(1,n+1,1):
    p=int(input('Valor de p: '))
    a.append(p)
g=int(input(' P de entrada: '))
h=int(input('P de saída: '))
s=0
for j in range(g,h+1,1):
    s=s+a[j]
print(s)    

