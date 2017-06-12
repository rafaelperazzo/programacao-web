# -*- coding: utf-8 -*-

def pico(n):
    #CONTINUE...
    cont=0
    for i in range(0,len(n)-1,1):
        if n[i]<n[i]:
            cont=cont+1
            
        
    if cont>=1:
        return(True)
    else:
        return(False)

n = int(input('Digite a quantidade de elementos da lista: '))
#CONTINUE...

a=[]
for i in range(1,n+1,1):
    valor=int(input('Digite o elementos da lista:'))
    a.append(valor)
    
if pico(a)==True:
    print('S')
    
else:
    print('N')

    