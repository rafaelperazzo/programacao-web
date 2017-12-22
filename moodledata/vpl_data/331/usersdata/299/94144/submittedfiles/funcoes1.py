# -*- coding: utf-8 -*-

def crescente (lista):
    #escreva o código da função crescente aqui
    cont=0
    for i in range(1,len(lista),1):
        if lista[i-1]<lista[i]:
            cont=0
        else:
            cont+=1
    if cont>0:
        return('N')
    else:
        return('S')


#escreva as demais funções
def decrescente (lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i-1]>lista[i]:
            cont=0
        else:
            cont+=1
    if cont>0:
        return('N')
    else:
        return('S')

def iguais(lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i-1]==lista[i]:
            cont+=1
        else:
            cont=0
    if cont==0:
        return('N')
    else:
        return('S')
        
        
#escreva o programa principal
a=[]
b=[]
c=[] 
n_elementos=int(input('forneça quantos elementos as listas devem ter: '))
for i in range(0,n_elementos,1):
    a.append(int(input('Digite o elemento %d da lista a: ' %(i+1))))
for i in range(0,n_elementos,1):
    b.append(int(input('Digite o elemento %d da lista b: ' %(i+1))))
for i in range(0,n_elementos,1):
    c.append(int(input('Digite o elemento %d da lista c: ' %(i+1))))

print(crescente(a))
print(decrescente(a))
print(iguais(a))
print(crescente(b))
print(decrescente(b))
print(iguais(b))
print(crescente(c))
print(decrescente(c))
print(iguais(c))






















































