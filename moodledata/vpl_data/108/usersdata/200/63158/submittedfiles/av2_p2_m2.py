# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de salas:'))
t=[]
for i in range(0,n,1):
    x=int(input('Digite a quantidade de vidas:'))
    t.append(x)
h=int(input('Digite a sala de entrada:'))
p=int(input('Digite a sala de saida:'))
resultado=0
for i in range(h,p+1,1):
    resultado=resultado+t[i]
print(resultado)


