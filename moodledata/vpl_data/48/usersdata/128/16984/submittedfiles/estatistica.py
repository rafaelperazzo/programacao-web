# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def dpadrao(lista):
    somatorio = 0
    for i in range (0,len(lista),1):
        somatorio=somatorio+((lista[i]-media(lista)**2)
    dp=((1/(len(lista)-1))*somatorio)**0.5
    return dp
    
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
a=[]
b=[]
n=input('Digite a quantidade de termos: ')

for x in range (0,n,1):
    a.append(input('Digite um termo de A: '))

for y in range (0,n,1):
    b.append(input('Digite um termo de B: '))

media_a=media(a)
media_b=media(b)
dp_a=dpadrao(a)
dp_b=dpadrao(b)

print ('%.2f' %media_a)
print ('%.2f' %media_b)
print ('%.2f' %dp_a)
print ('%.2f' %dp_b)