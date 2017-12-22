# -*- coding: utf-8 -*-
n=int(input('Digite o número de seções horizontais da piscina: '))
while n<=1 or n>=10**5:
    print('Esse número é inválido!')
    n=int(input('Digite o número de seções horizontais da piscina: '))
h=int(input('Digite o número de seções verticais da piscina: '))
while h<=1 or h>=10**9:
    h=int(input('Digite o número de seções verticais da piscina: '))
matriz=[] 
for i in range(0,n,1):
   matriz.append(int(input('Digite o valor da seção: ') %d(i+1)))
  
print(matriz)    