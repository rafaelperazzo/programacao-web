# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
def desvio(lista):
    soma=0
    n=len(lista)
    for i in range(0,len(lista),1):
        soma=soma+((lista[i]-a)**2)
    desvio=((soma/n+1)**0,5)
    return desvio

n=int(input('digite n: '))
lista1=[ ]
for i in range(0,n,1):
    valor=float(input('digite n: '))
    lista1.append('valor')
lista2=[ ]
for i in range(0,n,1):
    valor=float(input('digite n: '))
    lista2.append('valor')
a= media(lista1)
b=media(lista2)
print(a)
#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 