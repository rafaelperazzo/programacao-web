# -*- coding: utf-8 -*-

def crescente (lista):
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            print('S')
        else:
            print('N')
    return

def decrescente(lista):
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            print('S')
        else:
            print('N')
    return

def igualdade(lista):
    for i in range(0,len(lista)-1,1):
        if lista[i]==lista[i+1] :
            print('S')
        else:
            print('N')
    return

n=int(input('digite a quantidade de elementos: '))

a=[]
b=[]
c=[]

for i in range(0,n):
    a.append(int(input('adicione elementos em a: ')))

for i in range(0,n):
    b.append(int(input('adicione elementos em b: ')))
    
for i in range(0,n):
    c.append(int(input('adicione elementos em c: ')))

print(crescente(a))
print(decrescente(a))
print(igualdade(a))

print(crescente(b))
print(decrescente(b))
print(igualdade(b))

print(crescente(c))
print(decrescente(c))
print(igualdade(c))










    #escreva o código da função crescente aqui


#escreva as demais funções





#escreva o programa principal
