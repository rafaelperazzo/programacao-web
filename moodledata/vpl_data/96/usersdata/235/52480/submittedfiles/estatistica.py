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
    n=len(lista)
    for i in range (0, len(lista), 1):
        soma=soma+(lista[i]-media(lista))**2
    soma=(soma/(n-1))**0.5
    return soma
    

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=int(input('digite o tamanho da lista 1:'))
a=[]
for i in range (0,n,1):
    numero=int(input('digite os numeros da lista:'))
    a.append(numero)
    
m=int(input('digite o tamanho da lista 2:'))
b=[]
for i in range (0,m,1):
    numero=int(input('digite os numeros da lista:'))
    b.append(numero)
amedia=media(a)
print('%.2f'%amedia)

adesvio=desvio(a)
print('%.2f'%adesvio)

bmedia=media(b)
print('%.2f'%bmedia)

bdesvio=desvio(b)
print('%.2f'%bdesvio)
