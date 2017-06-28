# -*- coding: utf-8 -*-

def media(a):
    soma = 0
    for i in range(0,len(a),1):
        soma = soma + a[i]
    media = soma/len(a)
    return (media)

#ESCREVA AS DEMAIS FUNÇÕES
def SomaA(X,Y):
    MediaX=Media[x]
    MediaY=Media[Y]
    soma=0
    for i in range(0,len(X),1):
        soma=soma+((X[i]-MediaX)*(Y[i]-MediaY))
    return(soma)
    
def Entrada(f):
    X=[]
    for i in range (0,f,1):
        valor=float(input('Digite o valor:'))
        X.append(valor)
    return X
 
  
def entradaLista(n):
    a = []
    for i in range(0,n,1):
        valor = float(input('Digite um valor: '))
        a.append(valor)
    return (a)

n = int(input('Digite o tamanho da lista: '))
x = entradaLista(n)
y = entradaLista(n)

p = somaA(X,Y)/((somaD(X)*somaD(y))**(0.5))

p = abs(p)

print('%.4f' % p)











