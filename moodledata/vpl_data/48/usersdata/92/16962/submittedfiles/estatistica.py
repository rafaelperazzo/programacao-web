# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def dv(x):
    soma2=0
    for i in range(0, len(x), 1):
        soma= soma+ (x(i)-media(x))**2
    desvio= (soma/(len(x)-1))**(1/2)
    return desvio

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n= int(input('Digite um valor: '))
x=[]
y= []

for i in range(0, n, 1):
    x.append(input('Digite um valor: '))
for i in range(0, n, 1):
    y.append(input('Digite um valor: '))
    
mediax= media(x)
dvx= dv(x)
mediay= media(y)
dvy= dv(y)

print ('%.2f' %mediax)
print ('%.2f' %dvx)
print ('%.2f' %mediay)
print ('%.2f' %dvy)





