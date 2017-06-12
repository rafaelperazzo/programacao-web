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
L=[]
for i in range (0,n,1):
    valor=float(input('digite o valor:'))
    L.append(valor)
R=[]
for i in range(0,n,1):
    valor=float(input('digite o valor:'))
    R.append(valor)

media1=media(L)
print(media1)
soma1=0
for i in range(0,n,1):
    soma1=soma1+((L[i]-media1)**2)
DP1=((soma1/(n-1))**0.5
print('%.2f' %DP1)
media2=media[R]
print(media2)
soma2=0
for i in range (0,n,1):
    soma2=soma2+(R[i]-media2)**2
DP2=((soma2/(n-1))**0.5
print('%.2f' %DP2)