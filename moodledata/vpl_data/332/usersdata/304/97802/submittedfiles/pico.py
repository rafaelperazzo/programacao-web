# -*- coding: utf-8 -*-
'''
def pico(a):
    #CONTINUE...
    conta = 0
    contb = 0
    contc = 0
    for i in range(1,len(a),1):
        if(a[i]>a[i-1]) and contb==0:
            conta=conta+1
        elif(a[i]<a[i-1]):
            contb=contb+1
        else:
            contc=contc+1
            break
    if conta + contb == len(a)-1:
        return(True)
    else:
        return(False)
n = int(input('Digite a quantidade de elementos da lista: '))
#CONTINUE...
a=[]

for i in range(0,n,1):
    v=int(input('Termo: '))
    a.append(v)
if pico(a)==True:
    print('S')
if pico(a)==False:
    print('N')
'''
def pico(lista):
    cont_a = 0
    cont_b = 0
    for in in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont_a = cont_a + 1
        else:
            break
    for in in range(cont_b,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont_b = cont_b + 1
        else:
            break    
    if cont_a + cont_b == len(lista)-1 and cont_a>0 and cont_b>0:
        return('S')
    else:
        return('N')
lista=[]
n = int(input('Digite a quantidade de elementos da lista: '))
for in in range(0,n,1):
    lista.append(int(input('Digite n: ')
print(pico(lista))
        