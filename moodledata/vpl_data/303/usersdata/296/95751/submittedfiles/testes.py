# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#ENTRADA
...
n = int(input("Digite o valor de n: "))
a = []
for i in range(0,n,1):
    a.append(int(input('Digite um valor: ')))
media = sum(a)/len(a)
soma = 0
for i in range(0,n,1):
    soma += (a[i] - media)**2
    desvio = ((1/(n-1)*soma))**0.5 
print(desvio)
...
    
