# -*- coding: utf-8 -*-


def media(a):
    soma = 0
    for i in range(0,len(a),1):
        soma = soma+a[i]
    resultado = soma/len(a)
    return resultado

def desvio(a,m):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+((a[i]-m)**2)
    
    desvio=(soma/len(a)-1)**0.5
    return desvio
    
n=int(input('Quantidade de elementos das listas:'))
a=[]

for i in range (0,n,1):
    valor=(input('Valor de a:'))
    a.append(valor)

b=[]

for i in range (0,n,1):
    valor=(input('Valor de b:'))
    b.append(valor)

ma= media(a)
da= desvio(a,ma)
mb= media(b)
db= desvio(b,mb)

print('%.2f'%ma)
print('%.2f'%da)
print('%.2f'%mb)
print('%.2f'%db)