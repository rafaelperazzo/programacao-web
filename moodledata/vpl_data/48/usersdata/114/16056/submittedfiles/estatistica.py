# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    media1 = soma/len(lista)
    return media1
#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desviop(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+((lista[i] - media(lista))**2)
    desviop1= (soma/(len(lista)-1))**0.5
    return desviop1

n=input('digite o valor de n: ')
a=[]
b=[]
for i in range (0,n,1):
    a.append(input('digite os n valores para a lista a: '))
    
for i in range (0,n,1):
    b.append(input('digite os n valores para a lista b: '))
media_a=media(a)
media_b=media(b)
s_a=desviop(a)
s_b=desviop(b)

print ('%.2f' %media_a)
print ('%.2f' %s_a)
print ('%.2f' %media_b)
print ('%.2f' %s_b)
    

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 