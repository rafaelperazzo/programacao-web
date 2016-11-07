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
def desviopadrão(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+(((lista[i] - media(lista))**2)
    dp=((1/(n-1))*soma)**(1/2)
    return dp
    
a=[]
b=[]
n=input('Dig n:')

for i in range(0,n,1):
    a.append(input('a:'))
for i in range(0,n,1):
    b.append(input('b:'))

media_a=media(a)
media_b=media(b)
dp_a=desviopadrão(a)
dp_b=deviopadrão(b)

print media_a
print dp_a
print media_b
print dp_b






        