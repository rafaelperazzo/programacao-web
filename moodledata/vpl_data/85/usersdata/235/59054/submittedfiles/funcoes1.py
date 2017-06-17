# -*- coding: utf-8 -*-

def crescente (lista):
    #escreva o código da função crescente aqui
    contador=0
    for i in range(1,len(lista),1):
        if lista[i]<lista[i-1]:
            contador=contador+1
    if contador==0:
        return True
    else:
        return False
def decrescente (lista):
    condador=0
    for i in range(0,len(lista),1):
        if lista[i]<lista[i+1]:
            contador=contador+1
        if len(lista)==contador:
            return True
        else:
            return False
def consecultivo (lista):
    contador=0
    for i in range(0,len(lista),1):
        if lista[i]==lista[i+1]:
            contador=contador+1
        if contador=!0:
            return True
        else:
            return false
    

#escreva as demais funções
n=int(input('digite o tamanho da lista:'))
a=[]
for i in range(1,n,1):
    x=int(input('digite um numero:'))
    a.append(x)
if crescente (a)=true:
    print('s')




#escreva o programa principal
