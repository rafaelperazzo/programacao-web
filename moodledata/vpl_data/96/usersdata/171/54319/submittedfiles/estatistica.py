# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desvio(lista):
    n=len(lista)
    soma2=0
    for i in range(0,len(lista),1):
        soma2 = soma2 + (lista[i]-resultado)**2
    desvio padrao = (soma2/(n-1))**(0,5)
    return desvio padrao
m=int(input('digite o numero de elementos da lista:'))
a=[]
b=[]
for i in range(1,m+1,1):
    valor A=int(input('digite os numero da lista a:'))
    a.append(valor A)
    valor B=int(input('digite os numero da lista b:'))
    b.append(valor B)
print ('%.2f'%def media(a))
print ('%.2f'%def desvio(a))
print ('%.2f'%def media(b))
print ('%.2f'%def desvio(b))
    

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 