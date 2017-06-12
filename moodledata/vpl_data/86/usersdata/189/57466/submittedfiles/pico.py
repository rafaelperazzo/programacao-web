# -*- coding: utf-8 -*-
def pico(lista):
   if w[0]<w[1]:
       cont=1
       x=0
       while cont<n:
           if x==0:
               if w[cont]<w[cont-1]:
                   x=1
           if x==1:
                if w[cont]>w[cont-1]:
                    x=2
            else:
                return (2)
            cont=cont+1
        return (1)
    else:
        return (2)
n = input('Digite a quantidade de elementos da lista: ')
w=[]
y=0
while y<n:
    valor= int(input('número:'))
    a.append(valor)
    y=y+1
if pico (w)==1:
    print ('S')
else:
    print ('N')
    

