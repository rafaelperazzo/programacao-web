# -*- coding: utf-8 -*-

def media(a):
    soma = 0
    for i in range(0,len(a),1):
        soma = soma + a[i]
    media = soma/len(a)
    return (media)

#ESCREVA AS DEMAIS FUNÇÕES
def soma(a,b):
    ma=media(a)
    mb=media(b)
    soma=0
    for i in range(0,len(a),1):
        soma=soma+((a[i]-ma)*(b[i]-mb))
        return(soma)
    
def somaD(lista):
    mlista=media(lista)
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+(lista[i]-mlista)**2
        return(soma)
        
def entradaLista(n):
    a=[]
    for i in range(0,n,1):
        valor = float(input('Digite um valor:'))
        a.append(valor)
    return (a)
    
n=int(input('Digite o tamanho da lista:'))
x=entradaLista(n)
y=entradaLista(n)

p= soma(x,y)/(somaD(x)*somaD(y))**0.5

p= abs(p)

print('%.4f' % p)

        

        
