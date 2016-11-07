# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
    
def desvio(lista):
    s=0
    somatorio = 0
    for i in range(0,len(lista),1):
        s=((lista[i]-media)**2)+s
        x = s/(len(lista)-1)
        k = x**(1/2)
    return k
    
n=input("Digite a quantidade de termos:")
a = []
b = []

for i in range(0,n,1):
    a.append(input("Digite a lista A: "))
    
for i in range(1,n+1,1):
    b.append(input("Digite a lista B: "))
    
media_a = media(a)
media_b = media(b)
desa = desvio(a)
desb = desvio(b)

print ("%.2f" %media_a)
print ("%.2f" %media_b)
print ("%.2f" %desa)
print ("%.2f" %desb)


#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas.

