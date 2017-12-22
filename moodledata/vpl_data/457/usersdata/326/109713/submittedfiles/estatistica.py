# -- coding: utf-8 --
def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def dp(lista, resultado):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma +(( (lista[i] - resultado))**2.0/(len(lista)-1))
    soma = soma**(1/2.0)
    return soma
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
m = int(input('Digite listas: '))
n = int(input('Digite tamanho listas: '))
matriz = []
for i in range (m):
    v = []
    for j in range(n):
        v.append(int(input('digite valor: ')))
    matriz.append(v)
v = []
for i in range (m):
    v.append(  media(matriz[i])   )
    v.append(    dp(matriz[i], v[i*2])   )
for i in range(m*2):
    print ('%.2f'%(v[i]))