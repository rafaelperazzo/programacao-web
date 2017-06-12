# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desvio(lista):
    soma=0
    dp=0
    for i in range(0,len(lista),1):
        soma=soma+(lista[i]-media(lista))**2
    soma=(soma/((len(lista)-1)))**0.5
    return soma
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n1=int(input('digite o número de elemetos da primeira lista:'))
l1=[]
i=0
while i<n1:
    elemento=float(input('digite um número:'))
    l1.append(elemento)
    i=i+1
n2=int(input('digite o número de elemetos da segunda lista:'))
l2=[]
i=0
while i<n2:
    elemento=float(input('digite um número:'))
    l2.append(elemento)
    i=i+1
m1=media(l1)
print('%.2f'%m1)
dp1=desvio(l1)
print('%.2f'%dp1)
m2=media(l2)
print('%.2f'%m2)
dp2=desvio(l2)
print('%.2f'%dp2)