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
        cont=cont+((lista[i]-media)**2)
    s=cont/(len(lista)-1)
    return s

n = input ('insira o valor de n:')    
a=[]
b=[]

for i in range (0,n,1):
    a.append(input('insira o valor:'))
    
for j in range (0,n,1):
    b.append(input('insira o valor:'))
    
media1=media(a)
media2=media(b)
desvio1=desvio(a)
desvio2=desvio(b)
print('%.2f'%media1)
print('%.2f'%desvio1)
print('%.2f'%media2)
print('%.2f'%desvio2)



#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 