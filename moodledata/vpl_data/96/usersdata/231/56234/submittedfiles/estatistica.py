# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def dp(lista):
    v=0
    d=0
    for i in range(0,len(lista),1):
        v=v+((lista[i]-media(lista))**2)
    d=(v/(len(lista)-1))**0.5
    return d
a=[]
b=[]
n=int(input('n: '))
for i in range(1,n+1,1):
    valor=float(input('v1:'))
    a.append(valor)
for i in range(1,n+1,1):
    valor=float(input('v2:'))
    b.append(valor)

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 

print('%.2f'%media(a))
print('%.2f'%dp(a))
print('%.2f'%media(b))
print('%2.f'%dp(b))

