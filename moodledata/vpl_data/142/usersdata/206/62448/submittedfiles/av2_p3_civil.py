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
    
def soma(a):
    n=media(a)
    soma=0
    
    for i in range (0,len(a),1):
        soma=soma+((a[i]-a))**2
    return (soma)
 
  
def EntradaLista(n):
    a = []
    for i in range(0,n,1):
        valor = float(input('Digite um valor: '))
        a.append(valor)
    return (a)

n = int(input('Digite o tamanho da lista: '))
x = entradaLista(n)
y = entradaLista(n)

p = SomaA(X,Y)/((SomaD(X)*SomaD(Y))**(0.5))

p = abs(p)

print('%.4f' % p)


o bixo tira foto, e ainda erra! MP








