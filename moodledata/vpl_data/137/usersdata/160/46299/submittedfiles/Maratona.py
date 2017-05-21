# -*- coding: utf-8 -*-

n=int(input('Digite o número de postos:'))
m=int(input('Digite a distância determinada máxima:'))
i=0
cont=0
atual=0
proximo=0
for i in range(1,n,1):
    proximo=int(input('Digite a entrada:'))
    if proximo-atual>m:
        cont=cont+1
        atual=proximo
        print('N')
