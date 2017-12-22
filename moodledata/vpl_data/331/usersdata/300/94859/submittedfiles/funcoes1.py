# -*- coding: utf-8 -*-

def crescente (n,lista):
    #escreva o código da função crescente aqui
    for i in range(1,n,1):
        p = 0
        if lista[i-1] > lista[i]:
            p = p+1
    if p == n:
        return True
    else:
        return False
        
#escreva as demais funções






#escreva o programa principal
n = int(input('Digite a quantidade de elementos das listas: '))
a = []
b = []
c = []

if crescente(n,a):
    print('S')
else:
    print('N')
    
if crescente(n,b):
    print('S')
else:
    print('N')    
    
if crescente(n,c):
    print('S')
else:
    print('N')

