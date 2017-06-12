# -*- coding: utf-8 -*-

def pico(n):
    #CONTINUE...
    con=0
    for i in range(0,len(n)-1,1):
        if n[i]<n[i+1]<n[i+2]:
            cont=cont+1
            return true
        else:
            return(False)
            
    


n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...

a=[]
for i in range(1,n+1,1):
    valor=int(input('digite o elementos da lista:'))
    a.append(valor)
    
if pico(a)==True:
    print('S')
else:
    print('N')
