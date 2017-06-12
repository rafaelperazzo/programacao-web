# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas.

n=int(input('Informe o número de termos na lista: '))

lista1=[]
for i in range(0,n,1):
    numero=float(input('Informe os números da primeira lista: '))
    lista1.append(numero)

lista2=[]
for i in range(0,n,1):
    numero=float(input('Informe os números da segunda lista: '))
    lista2.append(numero)

media1=media(lista1)
print(media1)
somatorio1=0
for i in range(0,n,1):
    somatorio1=somatorio1+((lista1[i]-media1)**2)
desvioPadrao1=((somatorio1/(n-1))**0.5)
print('%.2f' %desvioPadrao1)

media2=media(lista2)
print(media2)
somatorio2=0
for i in range(0,n,1):
    somatorio2=somatorio2+((lista2[i]-media2)**2)
desvioPadrao2=((somatorio2/(n-1))**0.5)
print('%.2f' %desvioPadrao2)