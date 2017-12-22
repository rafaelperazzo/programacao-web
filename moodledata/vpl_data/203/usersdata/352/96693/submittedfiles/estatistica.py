# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 

def desvio_padrao(lista):
    for i in range (0,len(lista),1):
        somatorio=somatorio+((a[i]-media(lista))**2)
    somatorio=((1/(len(lista)-1))*somatorio)**0.5
    return (somatorio)

n=int(input('Quantidade de elementos: '))
lista_a=[ ]
lista_b=[ ]

for i in range(0,n,1):
    valor=float(input('Valor: '))
    lista_a.append(valor)

for i in range(0,n,1):
    valor=float(input('Valor: '))
    lista_b.append(valor)
    
print('%.2f' %media(lista_a))
print('%.2f' %desvio_padrao(lista_a))
print('%.2f' %media(lista_b))
print('%.2f' %desvio_padrao(lista_b))