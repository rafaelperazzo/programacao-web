# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def desviopadrao(lista):
    soma=0
    if media(lista):
        m=media(lista)
        for i in range(0,len(lista),1):
            soma=soma+(lista[i]-m)**2
            i=i+1
        desvio=((1/(n-1))*soma)**0.5
    return desvio
n=int(input('digite o numero de elemenos da lista:'))
soma=0
i=0
a=[]
b=[]
for i in range(0,n,1):
    p=float(input('digite o valor:'))
    a.append(p)
    i=i+1
for i in range(0,len(a),1):
    soma=soma+a[i]
    i=i+1
for i in range(0,n,1):
    q=float(input('digite o valor da segunda lista:'))
    b.append(q)
    i=i+1
for i in range(0,len(a),1):
    soma=soma+b[i]
    i=i+1
if media(a):
    print ('%.2f' %media(a))
if desviopadrao(a):
    print ('%.2f' %desviopadrao(a))
if media(b):
    print ('%.2f' %media(b))
if desviopadrao(b):
    print ('%.2f' %desviopadrao(b))



#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 