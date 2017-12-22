# -*- coding: utf-8 -*
def crescente (d,lista):
    cont=0
    for i in range (0,d-1,1):
        if lista[i]<lista[i+1]:
            cont= cont+1
    if cont==(len(lista)-1):
        return('S')
    else:
        return('N')
        
def decrescente (d,lista):
    cont=0
    for i in range (0,d-1,1):
        if lista[i]>lista[i+1]:
            cont= cont+1
    if cont==(len(lista)=1):
        return('S')
    else:
        return('N')
        
def consecutivo(d,lista):
    cont=0
    for i in range (0,d-1,1):
        if lista[i]==lista[i+1]:
            cont= cont+1
    if cont>0:
        return('S')
    else:
        return('N')
        
n= int(input('Digite a quantidade de termos de cada lista:'))
a= []
b= []
c= []

for i in range (0,n,1):
    valorA= float('Digite os valores da lista a:'))
    a.append(valorA)
for i in range (0,n,1):
    valorB= float('Digite os valores da lista b:'))
    b.append(valorB)
for i in range (0,n,1):
    valorC= float('Digite os valores da lista c:'))
    c.append(valorC)
    
print (crescente(n,a))
print (decrescente(n,a))
print (consecutivo(n,a))
print (crescente(n,b))
print (decrescente(n,b))
print (consecutivo(n,b))
print (crescente(n,c))
print (decrescente(n,c))
print (consecutivo(n,c))



    