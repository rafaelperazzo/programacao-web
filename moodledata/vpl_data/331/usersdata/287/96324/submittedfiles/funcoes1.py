# -*- coding: utf-8 -*-

def crescente(n,lista_crescente):
    cont_cresce=0
    for i in range(0,n-1,1):
        if lista_cresce[i]<lista_cresce[i+1]:
            cont_cresce+=1
    if cont_cresce==len(lista_cresce)-1:
        return ("S")
    else:
        return ("N")
    
    #escreva o código da função crescente aqui
def decresce(n,lista_decresce):
    cont_decresce=0
    for i in range(0,n-1,1):
        if lista_decresce[i]>lista_decresce[i+1]:
            cont_decresce+=1
    if cont_decresce==len(lista_decresce)-1:
        return ("S")
    else:
        return ("N")
        
def conse(n,lista_conse):
    cont_conse=0
    for i in range(0,n-1,1):
        if lista_conse[i]==lista_conse[i+1]:
            cont_conse+=1
        if cont_conse>0:
            return("S")
        else:
            return("N")
            

#escreva as demais funções

print(cresce(6,[1,2,3,4,5,6]))
print(decrece(6,[1,2,3,4,5,6]))
print(conse(6,[1,2,3,4,5,6]))
print(cresce(6,[7,6,5,4,3,2]))
print(decrece(6,[7,6,5,4,3,2]))
print(conse(6,[7,6,5,4,3,2]))
print(cresce(6,[9,8,8,8,9,1]))
print(decrece(6,[9,8,8,8,9,1]))
print(conse(6,[9,8,8,8,9,1]))




#escreva o programa principal
