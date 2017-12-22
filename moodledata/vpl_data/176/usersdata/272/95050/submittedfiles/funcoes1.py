# -*- coding: utf-8 -*-



def crescente (lista):
    #escreva o código da função crescente aqui
    for i in range (0,len(lista),1):
        if (i==0):
            if (a[i]<a[i+1]):
                cont=cont+1
        elif (i==(len(lista)-1)):
            if (a[i-1]<a[i]):
                cont=cont+1
        else:
            if (a[i]<a[i+1]):
                cont=cont+1
    if (cont==(len(lista)-1)):
        return(True)
    else:
        return(False)

#escreva as demais funções





#escreva o programa principal

n = int(input('Digite o número de elementos das listas: '))
a=[]
b=[]
c=[]

for i in range (0,n,1):
    a.append(int(input('Digite o valor: ')))
    b.append(int(input('Digite o valor: ')))
    c.append(int(input('Digite o valor: ')))
print(a)
print(b)
print(c)








