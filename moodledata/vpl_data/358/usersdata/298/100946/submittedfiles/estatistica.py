# -*- coding: utf-8 -*-
def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def desvpad(lista):
    soma = 0
    for i in range (0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    somat = 0
    for i in range (0, len(lista), 1):
        somat = somat + ((lista[i] - resultado)**2)
    d = float(((1/(len(lista)-1))*somat))**(float(1/2))
    return d

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=int(input('Digite o número de linhas da matriz: '))
m=int(input('Digite o número de colunas da matriz: '))

matriz=[]
for i in range (0, n, 1):
    linha=[]
    for j in range (0, m , 1):
        linha.append(int(input('Digite um elemento: ')))
    matriz.append(linha)

for i in range (0, n, 1):
    k=media(matriz[i])
    print('%.2f' & k)
    l=desvpad(matriz[i])
    print('%.2f' % l)