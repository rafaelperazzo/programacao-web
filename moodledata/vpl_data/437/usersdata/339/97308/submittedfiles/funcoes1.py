# -*- coding: utf-8 -*-

def crescente (lista):
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            print('S')
        else:
            prnt('N')
    return

def decrescente(lista):
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            print('S')
        else:
            prnt('N')
    return

def igualdade(lista):
    for i in range(0,len(lista)-1,1):
        if lista[i]==lista[i+1] and lista[i]==lista[i-1]:
            print('S')
        else:
            prnt('N')
    return

a=[]
b=[]
c=[]

a.append(int(input('adicione elementos em a: ')))
b.append(int(input('adicione elementos em b: ')))
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
