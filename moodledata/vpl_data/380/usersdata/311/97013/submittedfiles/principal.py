# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
a=[]
n=int(input('Digite o numero: '))
for i in range (0,n,1):
    a.append(str(input('Digite o numero%d: ' %(i+1))))
b=str(a.sort())

def crescente(lista):
    for i in range (0,n):
        while lista[i]<lista[i+1] and lista[i+1]<lista[i+2]:
            return 'S'
        else:
            return 'N'


print (crescente(a))
        







#a=[]
#def crescente(lista):
 #   for i in range (0,n,1):
  ##         return 'S'
    ############