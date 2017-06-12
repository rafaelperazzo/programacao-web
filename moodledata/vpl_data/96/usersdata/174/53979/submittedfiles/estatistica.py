# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def dp(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + ((lista[i] - media(lista))**2)
    resultado = (soma/(len(lista)-1))**0.5
    return resultado
a=[]
b=[]
n=int(input('Quantidade de elementos: '))
for i in range(1,n+1,1):
    valor=float(input('1ª Lista/ %dºValor: '%i))
    a.append(valor)
for i in range(1,n+1,1):
    valor=float(input('2ª Lista/ %dºValor: '%i))
    b.append(valor)
print('%.2f'%media(a))
print('%.2f'%dp(a))
print('%.2f'%media(b))
print('%.2f'%dp(b))
#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 