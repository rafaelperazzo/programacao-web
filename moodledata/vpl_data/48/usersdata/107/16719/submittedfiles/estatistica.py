# -*- coding: utf-8 -*-
from __future__ import division

def desvio(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma= soma + lista[i]
    resultado=soma/len(lista)
    return resultado
des desvio(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+(lista[i]-media(lista))**2
    resultado=(soma/len(lista)-1))**0,5
    return resultado
    
a=[]
b=[]
n=input('digite o valor de n:')
for i in range(0,n,1):
    a.append(input('digite um elemento de a:'))
for i in range(0,n,1):
    b.append(input('digite um elemento de b:')
ma=media(a)
mb=media(b)
Da=desvio(a)
Db=desvio(b)
print('%.2f'%Ma)
print('%.2f'%Da)
print('%.2f'%Mb)
print('%.2f'%Db)
    

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 