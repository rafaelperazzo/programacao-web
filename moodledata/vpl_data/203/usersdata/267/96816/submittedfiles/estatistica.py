# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desvio(a,media):
    somat=0
    for i in range(0,len(a),1):
        somat=somat+(a[i]-media)**2
    s=((1/(len(a)-1))*somat)**0.5
    return(s)

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=int(input('Quant de elementos: '))
a=[]
b=[]
print('LISTA 1: ')
for i in range(0,n,1):
    a.append(float(input('Digite os elementos da lista 1: ')))
print()
print('LISTA 2: ')
for i in range(0,n,1):
    b.append(float(input('Digite os elementos da lista 2: ')))
media_a=media(a)
media_b=media(b)
dev_a=desvio(a,media_a)
dev_b=desvio(b,media_b)
print('%.2f' %media_a)
print('%.2f' %media_b)
print('%.2f' %dev_a)
print('%.2f' %dev_b)