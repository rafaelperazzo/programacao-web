# -*- coding: utf-8 -*-

def crescente (a):
    #escreva o código da função crescente aqui
    for i in range (0,len(a)-1,1):
        if (a[i] < a[i+1]):
            return 'S'
        else:
            return 'N'

#escreva as demais funções
def descrescente (a):
    for i in range (0,len(a)-1,1):
        if (a[i] > a[i+1]):
            return 'S'
        else:
            return 'N'
            
def el_iguais (a):
    cont= 0
    for i in range (0,len(a)-1,1):
        if (a[i]==a[i+1]):
            cont +=1
    if (cont > 0):
        return 'S'
    else:
        return 'N'
        
'''
#escreva o programa principal
n= int(input('Digite quantidade de elementos da lista: '))
a= []
for i in range(0,6,1):
    a.append(int(input('Digite um valor: ')))
b= []
for i in range(0,6,1):
    b.append(int(input('Digite um valor: ')))
c= []
for i in range(0,6,1):
    c.append(int(input('Digite um valor: ')))
'''
a=[1,2,3,4,5]
b=[7,6,5,4,3,2]
c=[9,8,8,8,9,1]

print(crescente(a))
print(descrescente(a))
print(el_iguais(a))

print(crescente(b))
print(descrescente(b))
print(el_iguais(b))

print(crescente(c))
print(descrescente(c))
print(el_iguais(c))

