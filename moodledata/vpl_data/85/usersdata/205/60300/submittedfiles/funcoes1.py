# -*- coding: utf-8 -*-

def cres(lista):
  for j in range (0, len(lista)-1, 1):
      if (lista[j]>lista[j+1]):
          return(False)
    return(True)
    
def decres(lista):
    for j in range (0, len(lista)-1, 1):
        if (lista[j]<lista[j+1]):
            return(False)
    return(True)
    
    def iguais(lista):
        cont=0
        for j in range (0, len(lista)-1, 1):
            if (lista[j]==lista[j+1]):
                cont=cont+1
        if (cont>=1):
            return(True)
        else:
            return(False)
            
n=int(input('digite a quantidade de elementos das listas:'))
a=[]
b=[]
c=[]
for i in range (1, n+1, 1):
    valor=int(input('digite os elementos da lista A:'))
    a.append(valor)
for i in range (1, n+1, 1):
    valor=int(input('digite os elementos da lista B:'))
    b.append(valor)
for i in range (1, n+1, 1):
    valor=int(input('digite os elementos da lista C:'))
    c.append(valor)
if (cres(a)):
    print('S')
else:
    print('N')
if (decres(a)):
    print('S')
else:
    print('N')
if  (iguais(a)):
    print('S')
else:
    print('N')
if (cres(b)):
    print('S')
else:
    print('N')
if (decres(b)):
    print('S')
else:
    print('N')
if  (iguais(b)):
    print('S')
else:
    print('N')
if (cres(c)):
    print('S')
else:
    print('N')
if (decres(c)):
    print('S')
else:
    print('N')
if  (iguais(c)):
    print('S')
else:
    print('N')
    









