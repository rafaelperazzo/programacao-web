# -*- coding: utf-8 -*-

def crescente (lista):
    #escreva o código da função crescente aqui
def crescente(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False
#escreva as demais funções
def descrescente(lista):
    cont=0
    for i in range(1,len(lista),1)):
        if lista[i]>lista[i-1]:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False
def consecutivo(lista):
    cont=0
    for i in range(0,len(lista),1)):
        if lista[i]==lista[i+1] or lista[i]==lista[i-1]:
            cont=cont+1
    if cont!=0:
        returne False
    else:
        return True
#escreva o programa principal
n=int(input('Digite o número de elementos: '))
a=[]
for i in range(1,n+1,1):
    an=int(input('Digite um número: '))
    a.append(an)
b=[]
for i in range(1,n+1,1):
    bn=int(input('Digite um número: '))
    b.append(bn)
c=[]
for i in range(1,n+1,1):
    cn=int(input('Digite um número: '))
    c.append(cn)
if crescente(a):
    print('S')
elif crescente(a):
    