# -*- coding: utf-8 -*-

def media(v):
    soma = 0
    for i in range(0,len(a),1):
        soma = soma + v[i]
    media = soma/len(v)
    return (media)

#ESCREVA AS DEMAIS FUNÇÕES
def somaV(x,y):
    mx=media(x)
    my=media(y)
    soma=0
    for i in range (0,len(x),1):
        soma=soma+((x[i]-mx)*(y[i]-my))
    return soma
    
def soma(v):
    m=media(v)
    soma=0
    for i in range (0,len(v),1):
        soma=soma+((v[i]-m))**2
    return (soma)
    
def entrada lista(n):
    v=[]
    for i in range(0,n,1):
        valor=float(input('escreva um valor:'))
        v.append(valor)
    return (v)
    
    
n=int(input('escreva o tamanho da lista:'))
x= entrada lista(n)
y= entrada lista(n)

u=somaV(x,y)//((soma(x)*soma(y))**(0.5))

u=abs(u)

print('%.4f'%p)
def entradaLista(n):
    a = []
    for i in range(0,n,1):
        valor = float(input('Digite um valor: '))
        a.append(valor)
    return (a)

n = int(input('Digite o tamanho da lista: '))
x = entradaLista(n)
y = entradaLista(n)

p = #CALCULE O VALOR DE P

p = abs(p)

print('%.4f' % p)
