# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
    
def dpadrao(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + ((lista[i] - media(lista))**2)
    dp = ((1/(len(lista)-1))*soma)**(1/2)
    return dp
z = []
e = []
n = input('Digite o valor de n: ')

for i in range(0,n,1):
    z.append(input('Digite o valor de um elemento: '))
for i in range(0,n,1):
    e.append(input('Digite o valor de um elemento: '))
    
mediaz = media(z)
mediae = media(e)
dpz = dpadrao(z)
dpe = dpadrao(e)

print ('%.2f' %mediaz)
print ('%.2f' %dpz)
print ('%.2f' %mediae)
print ('%.2f' %dpe)

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 

