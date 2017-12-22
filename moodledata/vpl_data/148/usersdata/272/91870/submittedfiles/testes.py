# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

def MG(a):
    produto=1
    for i in range(0,len(a),1):
        produto=produto*a[i]
    produto=produto**(1/len(a))
    return(produto)

n=int(input('Digite a quantidade de elementos da lista: '))
a=[]
for i in range(0,n,1):
    valor=float(input('Digite um valor: '))
    a.append(valor)
print(MG(a))
    
    

    

