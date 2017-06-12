# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def dp(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma = soma + ((lista[i]-media(lista))**2)
    desvio = (soma/(n-1))**0.5
    return desvio

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=int(input('tamando da lista: '))
l1=[]
l2=[]
for i in range(1,n+1,1):
    a=float(input('elemento lista 1: '))
    b=float(input('elemento lista 2: '))
    l1.append(a)
    l2.append(b)
m1=media(l1)
m2=media(l2)
dp1=dp(l1)
dp2=dp(l2)
print('%.2f' % m1)
print('%.2f' % dp1)
print('%.2f' % m2)
print('%.2f' % dp2)