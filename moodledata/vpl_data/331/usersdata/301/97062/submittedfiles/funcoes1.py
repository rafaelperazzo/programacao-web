# -*- coding: utf-8 -*-


    #escreva o código da função crescente aqui
def cresce(n,lista-cresce):
    cont_cresce=0
    for i in range(0,n-1,1):
        if lista_cresce[i]<lista_cresce[i+1]:
            cont_cresce+=1
    if cont_cresce==len(lista_cresce)-1:
        return ('S')
    else:
        return ('N')


#escreva as demais funções

def decresce(n,lista_descresce):
    cont_decresce=0
    for i in range (0,n-1,1):
        if lista_decresce[1]>lista_decresce[i+1]:
            cont_decresce+=1
    if cont decresce==len(lista_decresce)-1:
        return ('S')
    else:
        return ('N')
        
def conse(n,lista_conse):
    cont_conse=0
    for i in range(0,n-1,1):
        if lista_conse[i]==lista_conse[i+1]:
            cont_conse+=1
    if cont_conse>0:
        return('S')
    else:
        return ('N')
            

#escreva o programa principal
a=[]
b=[]
c=[]
n=int(input('digite os valores da lista: '))
for i in range(0,n,1):
    a.append(float(input('digite os valores de a: ')))
for i in range(0,n,1):
    b.append(float(input('digite os valores de b: ')))
for i in range(0,n,1):
    c.append(float(input('digite os valores de c: ')))
print(cresce(n,a))
print(decresce(n,a))
print(conse(n,a)
print(cresce(n,b))
print(decresce(n,b))
print(conse(n,b)
print(cresce(n,c))
print(decresce(n,c))
print(conse(n,c)
       









A
