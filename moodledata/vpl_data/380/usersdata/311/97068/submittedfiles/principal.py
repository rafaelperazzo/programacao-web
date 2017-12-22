# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
a=[1,1,3]
sort=True
i=1
n=int(input('Digite o numero: '))
def descrecente(lista):
    for i in range(0,n,1):
        while lista[i]<lista[i+1]:
            return True
        else:
            return False
if (descrecente(a))==True:
    print ('S')
else:
    print ('N')
        





#a=[]
#def crescente(lista):
 #   for i in range (0,n,1):
  ##         return 'S'
    ############