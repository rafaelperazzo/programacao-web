# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def dp(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+(lista[i]**2)-(media(lista)**2)
    resultado=soma/len(lista)
    return resultado
a=[]
n=int(input('Quantidade de elementos:'))
for i in range(1,n+1,1):
    valor=float(input('%dºValor:'%i))
    a.append(valor)
b=[]
for i in range(1,n+1,1):
    valor=float(input('%dºValor:'%i))
    b.append(valor)
print(media(a))
print(dp(a))
print(media(b))
print(dp(b))
#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 