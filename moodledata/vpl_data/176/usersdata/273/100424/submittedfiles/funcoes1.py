# -*- coding: utf-8 -*-

def crescente (lista):
    #escreva o código da função crescente aqui
    cont=0
    for i in range (0,n-1,1):
        if (lista[i])<(lista[i+1]):
            cont=cont+1
        if cont==(n-1):
            return('S')
        else:
            return('N')
    

#escreva as demais funções
def consec(lista):
    cont=0
    for i in range(0,n-1,1):
        if (lista[i])==(lista[i+1])==0:
            cont=cont+1
            break
    if cont>0:
        return('S')
    else:
        return('N')
        
def decrescente(lista):
    cont=0
    for i in range(1,n,1):
        if (lista[(i-1)])>(lista[i]):
            cont=cont+1
    if cont==(n-1):
        return('S')
    else:
        return('N')

        

#escreva o programa principal
n=int(input('Digite a quantidade de termos da lista: '))
lista0=[]
print('1° Lista')
for  lista in range(0,n,1):
    num=float(input('Digite o numero da lista: '))
    lista0.append(num)

lista1=[]
print('2° lista')
for lista in range (0,n,1):
    num= float(input('Digite um numero da lista: '))
    lista1.append(num)

lista2=[]
for lista in range(0,n,1):
    num=float(input('Digite um numero da lista: '))
    lista2.append(num)

# Para lista 1
print(crescente(lista0))
print(decrescente(lista0))
print(consecut(lista0))

# Para lista 2
print(crescente(lista1))
print(decrescente(lista1))
print(consec(lista1))

# Para lista 3
print(crescente(lista2))
print(decrescente(lista2))
print(consec(lista2))

