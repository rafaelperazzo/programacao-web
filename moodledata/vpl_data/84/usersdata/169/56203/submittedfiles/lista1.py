# -*- coding: utf-8 -*-
n=int(input('Digite a Quantidade de Elementos da Lista:'))
l1=[]
somatoriopares=0
somatorioimpares=0
quantidadepares=0
quantidadeimpares=0
for i in range(1,n+1,1):
    v=int(input('Digite um Valor para a Lista:'))
    l1.append(v)
for k in range(0,len(l1),1):
    if (l1[k]%2==0):
        quantidadepares=quantidadepares+1
        somatoriopares=somatoriopares+l1[k]
    else: 
        quantidadeimpares=quantidadeimpares+1
        somatorioimpares=somatorioimpares+l1[k]
print(somatorioimpares)
print(somatoriopares)
print(quantidadepares)
print(quantidadeimpares)
print(l1)


