# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def dp(lista,resutado):
  soma = 0
  for i in range (0,len(lista),1):
    soma = soma + (((lista[i] - resultado))**2.0/(len(lista)-1))
  soma = soma**(1/2.0)
  return soma 

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
m = int(input('insira a quantidade de listas:'))
n = int(input('insira a quantidade de elementos:'))

mat = []
for i in range (m):
  v = []
  for j in range (n):
    v.append(int(input('digite os elementos:')))
  mat.append(v)
  
v =[]
for i in range (m):
  v.append(media(mat[i]))
  v.append(dp(mat[i],v[i*2]))
for i in range (m*2):
  print('%.2f'%(v[i]))