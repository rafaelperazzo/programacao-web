# -*- coding: utf-8 -*-

def crescente(lista):
    for i in range(0,len(lista)-1,1):
        while i in lista:
            if lista[i]<lista[i+1]:
                print('S')
                break
            elif lista[i]==lista[i+1] and lista[i]==lista[i-1]:
                print('N')
            else:
                print('N')
                break
    return 
'''
def decrescente(lista):
    for i in range(0,len(lista)-1,1):
        while i in lista:
            if lista[i]>lista[i+1]:
                print('S')
                break
            else:
                print('N')
                break
    return 

def igualdade(lista):
    for i in range(0,len(lista)-1,1):
        while i in lista:
            if lista[i]==lista[i+1] :
                print('S')
                break
            else:
                print('N')
                break
    return 
'''
n=int(input('digite a quantidade de elementos: '))

a=[]
#b=[]
#c=[]

for i in range(0,n):
    a.append(int(input('adicione elementos em a: ')))

#for i in range(0,n):
    #b.append(int(input('adicione elementos em b: ')))
    
#for i in range(0,n):
    #c.append(int(input('adicione elementos em c: ')))

crescente(a)
'''
decrescente(a)
igualdade(a)

crescente(b)
decrescente(b)
igualdade(b)

crescente(c)
decrescente(c)
igualdade(c)
'''









    #escreva o código da função crescente aqui


#escreva as demais funções





#escreva o programa principal
