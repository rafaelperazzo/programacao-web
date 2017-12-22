# -*- coding: utf-8 -*-
def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
def desvio(lista):
    from estatistica import media
    x=media(lista)
    for i in range(1,len(lista),1):
        soma+=(x-lista[i])**2
    resultado = (soma)**(1/2)/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
matriz=[]
m=int(input(''))
n=int(input(''))
for i in range(0,m,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(float(input('')))
        
for i in range(0,len(matriz),1):
    x=media(matriz[i])
    y=desvio(matriz[i])
    print('%.2f'%x)
    print('%.2f'%y)

