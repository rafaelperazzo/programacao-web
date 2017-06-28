# -*- coding: utf-8 -*-






n=int(input('n:'))
a=[]
for i in range(0,n,1):
    valor=int(input('valor:'))
    a.append(valor)
h=int(input('h:'))
j=int(input('j:'))

soma=0
for i in range(h,j+1,1):
    soma=soma+a[i]
print(soma)

