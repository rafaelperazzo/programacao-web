# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
a=[]
n=int(input('Digite o numero: '))
for i in range (0,n,1):
    a.append(str(input('Digite o numero%d: ' %(i+1))))
b=str(a.sort())

def crescente(lista,b):
    if lista==b:
        return True
    else:
        if lista<b or lista>b:
            return False
print (crescente(a,b))







#a=[]
#def crescente(lista):
 #   for i in range (0,n,1):
  ##         return 'S'
    ############