# -*- coding: utf-8 -*-
def somaMaior(a,x,y):
    soma=0
    for i in range(x,y+1,1):
        soma=soma+a[i]
    return(soma)

n=int(input('Digite o número de salas: '))

a=[]
for i in range(0,n,1):
    h=int(input('Digite o termo '+str(i)+' da lista: '))
    a.append(h)
    
x=int(input('Digite o índice da porta de entrada: '))
y=int(input('Digite o índice da porta de saída: '))


print(somaMaior(a,x,y))

        
        
        
        

