# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def desviopadrao(x):
    soma=0
    for i in range(0,len(x),1):
        soma=soma+(x[i]-m)**2
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
if media(a):
    print (media(a))
print (desviopadrao(a))


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 