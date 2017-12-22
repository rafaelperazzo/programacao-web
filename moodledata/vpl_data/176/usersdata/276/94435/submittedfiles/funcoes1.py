# -*- coding: utf-8 -*-

def crescente (lista):
    #escreva o código da função crescente aqui
    cont = 0
    for i in range (0,len (a),1):
        if (a[i+1] > a[i]):
            return (True)
        else:
            return (False)
            break
        
#escreva as demais funções
def decrescente (lista):
    cont = 0
    for i in range (0,len (a),1):
        if (a[i+1] < a[i]):
            return (True)
        else:
            return (False)
            break

def consec_iguais (lista):
    #escreva o código da função crescente aqui
    cont = 0
    for i in range (0,len (a),1):
        if (a[i+1] == a[i]):
            return (True)
            break
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
    
    
if consec_iguais (a):
    print ('N')
    print ('N')
    print ('S')

else:
    if crescente (a):
        print ('S')
    else:
        print ('N')

    if decrescente (a):
        print ('S')
    else:
        print ('N')
    print ('N')
    
if consec_iguais (b):
    print ('N')
    print ('N')
    print ('S')

else:
    if crescente (b):
        print ('S')
    else:
        print ('N')

    if decrescente (b):
        print ('S')
    else:
        print ('N')
    print ('N')

if consec_iguais (c):
    print ('N')
    print ('N')
    print ('S')

else:
    if crescente (c):
        print ('S')
    else:
        print ('N')

    if decrescente (c):
        print ('S')
    else:
        print ('N')
    print ('N')