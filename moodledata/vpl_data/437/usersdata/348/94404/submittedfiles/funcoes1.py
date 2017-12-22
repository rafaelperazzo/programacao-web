# -*- coding: utf-8 -*-


#escreva o código da função crescente aqui



#escreva as demais funções

def ad1(n):
    
    lista1 = []
    lista2 = []
    lista3 = []
    
    for i in range (0,n,1):
        lista1.append(int(input('digite o %d elemnto da lista1: ' % (1+i))))
    return lista1

def ad2(n):    
    for i in range (0,n,1):
        lista2.append(int(input('digite o %d elemnto da lista2: ' % (1+i))))
    return lista2

def ad3(n):
    for i in range (0,n,1):
        lista3.append(int(input('digite o %d elemnto da lista3: ' % (1+i))))    
    return lista3

#escreva o programa principal

n = int(input('informe a quantidade de elementos: '))


    

    
print (ad1(n))

print (ad2(n))

print (ad3(n))

    
    
    