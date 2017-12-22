# -*- coding: utf-8 -*-

def crescente (lista):
    #escreva o código da função crescente aqui
    cont = 0
    for i in range (0,len (lista),1):
        if (i==0):
            if (lista[i]<lista[i+1]):
                cont = cont + 1
        
        elif (i==(len(lista)-1)):
            if (lista[len(lista)-2]<lista[len(lista) - 1]):
                cont = cont +1
        
        else:
            if (lista[i-1]< lista[i] < lista [i+1]):
                cont = cont + 1
        
    if cont == len(lista):
        return (True)
    else:
        return (False)
            
        
#escreva as demais funções
def decrescente (lista):
    cont = 0
    for i in range (0,len (lista),1):
        if (i==0):
            if (lista[i]>lista[i+1]):
                cont = cont + 1
        
        elif (i==(len(lista)-1)):
            if (lista[i-1]>lista[i]):
                cont = cont +1
        
        else:
            if (lista[i-1]> lista[i] > lista [i+1]):
                cont = cont + 1
        
    if cont == len(lista):
        return (True)
    else:
        return (False)
            
            
def consec_iguais (lista):
    cont = 0
    for i in range (0,len (lista),1):
        if (i==0):
            if (lista[i]==lista[i+1]):
                cont = cont + 1
        
        elif (i==(len(lista)-1)):
            if (lista[i-1]==lista[i]):
                cont = cont +1
        
        else:
            if (lista[i]== lista[i+1]):
                cont = cont + 1
        
    if (cont != 0) :
        return (True)
    else:
        return (False)
        
#escreva o programa principal
n = int(input('Digite a quantidade de n:'))

a = []
b = []
c = []

for i in range (0,n,1):
    valor_a = float(input('Digite o elemento da primeira lista: '))
    a.append (valor_a)

for i in range (0,n,1):
    valor_b = float(input('Digite o elemento da segunda lista: '))
    b.append (valor_b)
    
for i in range (0,n,1):
    valor_c = float(input('Digite o elemento da terceira lista: '))
    c.append (valor_c)
    
    
if crescente (a):
    print ('S')
else:
    print ('N')

if decrescente (a):
    print ('S')
else:
    print ('N')

if consec_iguais (a):
    print ('S')
else:
    print ('N')

    
if crescente (b):
    print ('S')
else:
    print ('N')

if decrescente (b):
    print ('S')
else:
    print ('N')
    
if consec_iguais (b):
    print ('S')
else:
    print ('N')

if crescente (c):
    print ('S')
else:
    print ('N')

if decrescente (c):
    print ('S')
else:
    print ('N')
    
if consec_iguais (c):
    print ('S')
else:
    print ('N')