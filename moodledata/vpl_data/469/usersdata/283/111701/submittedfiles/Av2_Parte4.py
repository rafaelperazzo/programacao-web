# -*- coding: utf-8 -*-
M=int(input('Digite o valor de linhas: '))
N=int(input('Digite o valor de colunas: '))

while M<2 and M>1000:
    print('Numero invalido')
    M=int(input('Digite o valor de linhas: '))
while N<2 and N>1000:
    N=int(input('Digite o valor de colunas: '))

a=[]
at=[]
for i in range(0,M,1):
    l=[]
    for j in range(0,N,1):
        b=int(input('Digite o valor da quadra: '))
        while b<1 and b>100:
            print('Valor invalido')
            b=int(input('Digite o valor da quadra: '))
        l.append(b)
    a.append(l)
print(a)
            
    