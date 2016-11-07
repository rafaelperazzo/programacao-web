# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 

n = input('Tamanho do vetor: ')

i = 1
a = []
b = []

while n>=i:
    a.append(input('Digite o valor no vetor a: ')
    b.append(input('Digite o valor no vetor b: ')
    i = i+1
mediaa = sum(a)/n
mediab = sum(b)/n

j = 0
pa = 0
pb = 0
while n>j:
    pa = pa+(a[j]-mediaa)**2
    pb = pb+(b[j]-mediab)**2
    j = j+1
dpa = (pa/(n-1))**(1/2)
dpb = (pb/(n-1))**(1/2)

print('%.2f'% mediaa)
print('%.2f'% dpa)
print('%.2f'% mediab)
print('%.2f'% dpb)