# -*- coding: utf-8 -*-
'''
def crescente (lista):
    if lista == sorted(lista):
    return True
else:
    return False
def decrescente (lista):
    if lista == sorted(lista, reverse = True):
    return True
else:
    return False
def consectivos (lista,n):
    for i in range(0,n,1):
        if i < n:
            if lista[i-1] =! lista[i]
                return False
                continue
            else:
                return True
'''            
    #escreva o código da função crescente aqui


#escreva as demais funções





#escreva o programa principal
n = int(input('Digite o número de elementos das listas: '))
a = []
b = []
c = []
for i in range (0,n,1):
    a.append(int(input('Digite a%d: '%(i+1))))
for i in range(0,n,1):
    if i < n:
        if a[i-1] != a[i]:
            print('N')
            continue
        else:
            print('S')
'''
print(a)
for i in range (0,n,1):
    b.append(int(input('Digite b%d: '%(i+1))))
print(b)
for i in range (0,n,1):
    c.append(int(input('Digite c%d: '%(i+1))))
print(c)
'''
              
        
    
