# -*- coding: utf-8 -*-
n=int(input('digite n:'))
lista1=[]
lista2=[]
def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
def dp(lista):
    soma2=0
    for i in rage(0,len(lista),1):
        soma2=soma2+(lista[i]-media(lista))**2
    dp=(soma2/(len(lista)-1))**(0.5)
    return(dp)
for i in range(0,n,1):
    num=float(input('digite numero:'))
    lista1.append(num)
for i in range(0,n,1):
    num=float(input('digite numero:'))
    lista2.append(num)
print('%.2f'%media(lista1))
print('%.2f'%dp(lista1))
print('%.2f'%media(lista2))
print('%.2f'%dp(lista2))

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 