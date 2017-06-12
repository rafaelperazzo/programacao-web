# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 

n=int(input('digite n:'))
lista1=[]
for i in range (0,n,1):
    valor=float(input('digite o valor:'))
    lista1.append(valor)
    
lista2=[]
for i in range(0,n,1):
    valor=float(input('digite o valor:'))
    lista2.append(valor)

media1=media(lista1)
print(media1)

soma1=0
for i in range(0,n,1):
    soma1=soma1+(lista1[i]-media1)**2
desvioPadrao1=((soma1/(n-1))**0.5)
print('%.2f' %desvioPadrao1)

media2=media(lista2)
print(media2)

soma2=0
for i in range (0,n,1):
    soma2=soma2+(lista2[i]-media2)**2
desvioPadrao2=(soma2/(n-1))**0.5
print('%.2f' %desvioPadrao2)