# -*- coding: utf-8 -*-
k=int(input('NUMEROS DE PORTAS:'))
l=int(input('PORTA DE ENTRADA:'))
e=int(input('PORTA DE SAIDA:'))
a=[]
for i in range(0,k,1):
    g=int(input('VIDA:'))
    a.append(g)
soma=0
for i in range(l,e+1,1):
    soma=soma+a[i]
print(soma)



