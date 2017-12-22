# -*- coding: utf-8 -*-



def crescente (lista):
    #escreva o código da função crescente aqui
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont=cont+1
    if cont==(len(lista)-1):
        return (True)
    else:
        return (False)
        
  
    
#escreva as demais funções
def decrescente (lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont=cont+1
    if cont==(len(lista)-1):
        return (True)
    else:
        return (False)



def consecutivos (lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]==lista[i+1]:
            cont=cont+1
    if cont>=1:
        return (True)
    else:
        return (False)
        
        
#escreva o programa principal

n=int(input('Quantidade de elementos: '))
lista_a=[ ]
lista_b=[ ]
lista_c=[ ]

for i in range(0,n,1):
    valor=int(input('Valor da lista a: '))
    lista_a.append(valor)
    
for i in range(0,n,1):
    valor=int(input('Valor da lista b: '))
    lista_b.append(valor)
    
for i in range(0,n,1):
    valor=int(input('Valor da lista c: '))
    lista_c.append(valor)

    
    
if crescente(lista_a):
    print('S')
else:
    print('N')
    
if decrescente(lista_a):
    print('S')
else:
    print('N')    
if consecutivos(lista_a):
    print('S')
else:
    print('N')  
    
print() 
    
if crescente(lista_b):
     
    print('S')
else:
    print('N')
    
if decrescente(lista_b):
    print('S')
else:
    print('N')
    
if consecutivos(lista_b):
    print('S')
else:
    print('N')    
    
print()

if crescente(lista_c):
    print('S')
else:
    print('N')
    
if decrescente(lista_c):
    print('S')
else:
    print('N')    
if consecutivos(lista_c):
    print('S')
else:
    print('N') 
    
    
    