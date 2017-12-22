# -*- coding: utf-8 -*-
def media(lista):
  soma = 0
  for i in range(0,len(lista),1):
      soma = soma + lista[i]
  resultado = soma/len(lista)
  return resultado

# função para calcular o desvio padrão de uma lista
def desviPadrao(lista,resul):
  somat=0
  for i in range(0,len(lista),1):
    somat=(lista[i] - resul)**2 + somat
  desvio=(somat/len(lista))**0.5
  return desvio
    

#programa principal
qtlistas=int(input("Digite a quantidade de lista:"))
tam=int(input("Digite o tamanho:"))
matr=[]
for i in range(0,qtlistas,1):
  lis=[]
  for j in range(0,tam,1):
    lis.append(float(input("Digite um elemento para sua  lista:" )))
  matr.append(lis)

for h in range (0,len(matr),1):
    resul=media(matr[h])
    print("%.2f" % media(matr[h]))
    print("%.2f" % desviPadrao(matr[h],resul))
    
  
    
