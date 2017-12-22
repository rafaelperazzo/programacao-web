# -*- coding: utf-8 -*-
n=int(input('Digite o número de seções horizontais da piscina: '))
while n<=1 or n>=10**5:
    print('Esse número é inválido!')
    n=int(input('Digite o número de seções horizontais da piscina: '))
h=int(input('Digite o número de seções verticais da piscina: '))
while h<=1 or h>=10**9:
    print('Esse número é inválido!')
    h=int(input('Digite o número de seções verticais da piscina: '))
matriz=[] 
for j in range(0,h,1):    
    coluna=[]
    coluna.append(int(input('Digite o valor da seção vertical: ')))
for i in range(0,n,1):
    linha=[]
    linha.append(int(input('Digite o valor da seção horizontal: ' )))
print(linha)