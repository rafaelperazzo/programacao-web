# -*- coding: utf-8 -*-


def media(lista):
     media=sum(lista)/len(lista)
     return media 
def desvio_padrao(lista):
    somatorio=0
    for i in range(0,len(lista),1):
        somatorio=((media(lista) - lista[i])**2)+somatorio
    desvio = (somatorio/(n-1))**0.5
    return desvio
m=int(input('digite o valor de listas: '))
n=int(input('digite o numero de elementos de cada lista:  '))
matriz=[]
for i in range (0,m,1):
    matriz_linha=[]
    for j in range (0,n,1):
        matriz_linha.append(int(input('digite o elemento(%d,%d): '%(i+1,j+1))))
    matriz.append(matriz_linha)
    
for i in range(0,m,1):
    print(media(matriz[i]))
    print('%.2f'%(desvio_padrao(matriz[i])))
        
    
   

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 