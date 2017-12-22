# -*- coding: utf-8 -*-
n=int(input('Digite o número de seções horizontais da piscina: '))
while n<=1 or n>=10**5:
    print('Esse número é inválido!')
    n=int(input('Digite o número de seções horizontais da piscina: '))
h=int(input('Digite o número de seções verticais da piscina: '))
while h<=1 or h>=10**9:
    print('Esse número é inválido!')
    h=int(input('Digite o número de seções verticais da piscina: '))

for i in range(0,n,1):
    linha=[i]
    linha.append(int(input('Digite o %d valor da seção horizontal: ' %(i+1))))
for j in range(0,h,1):    
    coluna=[j]
    coluna.append(int(input('Digite o %d valor da seção vertical: ' %(j+1))))
print(linha,coluna)

