# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
    
def desvio(lista):
    cont=0
    for i in range (0,len(lista),1):
        cont=cont+(lista[i]-media(lista))**2
    s=cont/(len(lista))
    return s

n = input ('insira o valor de n:')    
a=[]
b=[]

for i in range (0,n,1):
    a.append(input('insira o valor:'))
    
for i in range (0,n,1):
    b.append(input('insira o valor:'))
    
m1=media(a)
m2=media(b)
d1=desvio(a)
d2=desvio(b)
print('%.2f'%m1)
print('%.2f'%d1)
print('%.2f'%m2)
print('%.2f'%d2)



#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 