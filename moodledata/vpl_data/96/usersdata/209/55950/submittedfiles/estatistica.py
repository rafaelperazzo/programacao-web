# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
def desvio(lista):
    somatorio=0
    for i in range(0,n,1):
        somatorio=somatorio+(lista[i]-media(lista))**2
    resultado=((1/(n-1))*somatorio)**0.5
    return resultado
n=int(input('Digite o tamanho da lista:'))
a=[]
b=[]
for i in range(0,n,1):
    x=float(input('Digite um valor para primeira lista:'))
    a.append(x)
for i in range(0,n,1):
    y=float(input('Digite um valor para segunda lista:'))
    b.append(y)

print('%.2f'%media(a))
print('%.2f'%desvio(a))
print('%.2f'%media(b))
print('%.2f'%desvio(b))