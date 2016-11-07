# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
def dp(lista, media):
    s=0
    for i in range(0,len(lista),1):
        s=s+(lista[i]-media)**2
    dp=(s/(n-1))**0.5
    return dp
a=[]
b=[]
n=int(input("Digite um número: "))
for i in range (0,n,1):
    a.append(input("Digite os termos de a: "))
for i in range (0,n,1):
    b.append(input("Digite os termos de b: "))
mediaA=media(a)
mediaB=media(b)
dpa=dp(a, mediaA)
dpb=dp(b, mediaB)
print ("%.2f" %mediaA)
print ("%.2f" %dpa)
print ("%.2f" %mediaB)
print ("%.2f" %dpb)

        
        
#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 