# -*- coding: utf-8 -*-






n=int(input('n:'))
a=int(input('a:'))
b=int(input('b:'))
for i in range(0,n,1):
    valor=int(input('valor:'))
    a.append(valor)
soma=0
for i in range(a,b+1,1):
    soma=soma+a[i]
print(soma)

