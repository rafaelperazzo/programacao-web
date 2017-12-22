# -*- coding: utf-8 -*-

def crescente (lista):
    #escreva o código da função crescente aqui
    cont=0
    for i in range(1,len(lista),1):
        
        if lista[i-1]<lista[i]:
            cont=0
        elif lista[i-1]==lista[i]:
            return('N')
            break
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
        elif lista[i-1]==lista[i]:
            return('N')
            break    
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
    if cont>0:
        return('S')
    else:
        return('N')
#escreva o programa principal
a=[]
b=[]
c=[] 
n_elementos=int(input(''))
for i in range(0,n_elementos,1):
    a.append(int(input('')))
for i in range(0,n_elementos,1):
    b.append(int(input('')))
for i in range(0,n_elementos,1):
    c.append(int(input('')))

print(crescente(a))
print(decrescente(a))
print(iguais(a))
print(crescente(b))
print(decrescente(b))
print(iguais(b))
print(crescente(c))
print(decrescente(c))
print(iguais(c))






















































