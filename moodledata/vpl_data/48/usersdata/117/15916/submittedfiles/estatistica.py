# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista

def desvio(lista):
    soma=0
    for i in range (0,n,1):
        soma=soma+(lista[i]-media)**2
    s=((1/(n-1))*soma)**(0.5)
    

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 

n=input('digite o valor de n:')

a=[]
b=[]

for i in range (0,n,1):
    a.append(input('Digite o valor da lista a:'))
    
for i in range (0,n,1):
    b.append(input('Digite o valor da lista b:'))
    
mediaa= media(a)
mediab= media(b)

desvioa= desvio(a)
desviob= desvio(b)

print ('%.2f'%mediaa)
print ('%.2f'desvioa)
print ('%.2f'mediab)
print ('%.2f'desviob)