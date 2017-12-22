# -*- coding: utf-8 -*-

def crescente (a):
    #escreva o código da função crescente aqui
    cont=0
    for i in range(1,len(a)+1,1):
        if a[i] > a[i-1]:
            cont=cont+1
        else:
            break
        if cont==len(a)-1:
            return(True)
        else:
            return(False)

#escreva as demais funções





#escreva o programa principal

n=int(input('Digite o numero de termos da primeira lista: '))
a=[]
for i in range(0,n,1):
    valor=int(input('Digite o termo : '))
    a.append(valor)
print(crescente(a))